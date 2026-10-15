"""ElevAd backend — FastAPI + RAG AI Copilot."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="ElevAd API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO(安全): 生产环境收紧为白名单
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProposalRequest(BaseModel):
    brand: str = Field(..., description="品牌名，如 Tims咖啡")
    budget: float = Field(..., gt=0, description="预算（万元）")
    goal: str = Field(..., description="一句话目标，如 北京写字楼推早餐")
    city: str = "北京"


class ProposalResponse(BaseModel):
    strategy: str
    copywriting: dict[str, str]  # 分时段文案 {morning: ..., afternoon: ...}
    budget_split: dict[str, float]
    references: list[str]        # RAG 引用的案例


@app.get("/api/health")
def health():
    return {"code": 0, "msg": "ok", "data": {"service": "elevad", "version": "0.1.0"}}


@app.post("/api/propose", response_model=ProposalResponse)
def propose(req: ProposalRequest):
    """Phase 2 实现：RAG 检索案例库 -> LLM 生成策略/文案/预算分配。
    当前为占位实现，验证前后端链路。"""
    return ProposalResponse(
        strategy=f"[占位] {req.brand} 在 {req.city} 以 {req.budget} 万元预算实现：{req.goal}",
        copywriting={
            "morning": "[占位] 早高峰 7:00-9:00 文案",
            "afternoon": "[占位] 午后 14:00-17:00 文案",
        },
        budget_split={"梯媒写字楼": 0.6, "社区智能屏": 0.25, "预留优化": 0.15},
        references=["[占位] 案例库建设中"],
    )
