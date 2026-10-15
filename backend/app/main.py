"""ElevAd backend — FastAPI + RAG AI Copilot.

定位（交叉验证后收窄）：不做投放决策（那是媒仓AI智投的事），
只做"销售提案物料生成"：策略摘要 + 分时段文案 + 案例引用。
"""
import json
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from . import rag

_INDEX: list[dict] = []


@asynccontextmanager
async def lifespan(app: FastAPI):
    """启动时构建向量索引（语料<100块，秒级完成）。"""
    _INDEX.extend(rag.build_index())
    yield


app = FastAPI(title="ElevAd API", version="0.2.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO(安全层): 生产收紧白名单
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProposalRequest(BaseModel):
    brand: str = Field(..., max_length=40, description="品牌名，如 Tims咖啡")
    budget: float = Field(..., gt=0, le=100000, description="预算（万元）")
    goal: str = Field(..., max_length=120, description="一句话目标，如 北京写字楼推早餐")
    city: str = Field(default="北京", max_length=20)


class ProposalResponse(BaseModel):
    strategy: str
    copywriting: dict[str, str]
    budget_split: dict[str, float]
    references: list[str]
    evidence: list[dict]  # RAG 命中的原文块（前端可展示"依据"）


@app.get("/api/health")
def health():
    return {"code": 0, "msg": "ok",
            "data": {"service": "elevad", "version": "0.2.0", "index_chunks": len(_INDEX)}}


@app.post("/api/propose", response_model=ProposalResponse)
def propose(req: ProposalRequest):
    if not _INDEX:
        raise HTTPException(503, "索引未就绪")
    query = f"{req.brand}，预算{req.budget}万元，{req.city}，目标：{req.goal}"
    hits = rag.retrieve(query, _INDEX, k=4)
    if not hits:
        raise HTTPException(422, "知识库未命中相关内容")
    raw = rag.generate(query, hits)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        raise HTTPException(502, "LLM输出解析失败")
    # LLM 偶尔返回嵌套结构，做一次展平归一化
    split = data.get("budget_split", {})
    flat: dict[str, float] = {}
    for k2, v in split.items():
        if isinstance(v, dict):
            for k3, v3 in v.items():
                flat[f"{k2}·{k3}"] = float(v3)
        else:
            try:
                flat[k2] = float(v)
            except (TypeError, ValueError):
                continue
    return ProposalResponse(
        strategy=data.get("strategy", ""),
        copywriting=data.get("copywriting", {}),
        budget_split=flat,
        references=data.get("references", []),
        evidence=[{"source": h["source"], "title": h["title"], "score": h["score"]} for h in hits],
    )
