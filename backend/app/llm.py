"""GLM (智谱) LLM 客户端 — OpenAI 兼容接口，纯 httpx 实现（零重依赖，便于在任何环境跑）。"""
import os
import json
import httpx

BASE_URL = os.getenv("LLM_BASE_URL", "https://open.bigmodel.cn/api/paas/v4")
API_KEY = os.getenv("LLM_API_KEY") or os.getenv("GLM_API_KEY", "")
CHAT_MODEL = os.getenv("LLM_MODEL", "glm-4-flash")   # 免费/低价档，演示足够
EMBED_MODEL = os.getenv("EMBED_MODEL", "embedding-2")


def chat(messages: list[dict], temperature: float = 0.7, json_mode: bool = False) -> str:
    """调用 GLM chat completions。messages=[{role, content}]"""
    body = {"model": CHAT_MODEL, "messages": messages, "temperature": temperature}
    if json_mode:
        body["response_format"] = {"type": "json_object"}
    r = httpx.post(
        f"{BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json=body, timeout=60,
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def embed(texts: list[str]) -> list[list[float]]:
    """批量计算 embedding 向量。"""
    r = httpx.post(
        f"{BASE_URL}/embeddings",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"model": EMBED_MODEL, "input": texts},
        timeout=60,
    )
    r.raise_for_status()
    data = sorted(r.json()["data"], key=lambda d: d["index"])
    return [d["embedding"] for d in data]
