# ElevAd (Tikin-3D 智投提案引擎)

**3D elevator ad simulator + AI proposal copilot — let clients see their DOOH campaign running before signing.**

> 国内首个专为电梯门投影打造的 Web 3D 沉浸式提案工作台——让大客户在签单前，先在手机里身临其境看到自己的广告在电梯里跑起来。

## 这是什么 / What is this

销售在客户面前输入三句话（品牌、预算、目标），2 分钟后客户在自己手机上看到自己的广告在 3D 电梯门上"跑起来"：

- **AI Copilot 层**（FastAPI + LangChain + RAG）：检索案例库 → 生成投放策略 + 分时段广告文案 + 预算分配
- **Tikin-3D 层**（Three.js + WebGL + VideoTexture）：电梯轿厢实景还原，双开门关合瞬间广告投射上门面，360° 交互
- **输出**：一份可微信转发的沉浸式提案 H5

## 技术栈 / Stack

| 层 | 技术 |
|---|---|
| 前端 | Vue 3 + Vite + Tailwind CSS |
| 3D | Three.js（@react-three/fiber 备选）、VideoTexture、OrbitControls |
| 后端 | FastAPI (Python) + Uvicorn |
| AI | GLM / OpenAI API、LangChain、FAISS 向量库、RAG |
| 部署 | Docker Compose、GitHub Actions CI、K8s manifests（规划中） |

## 快速开始 / Quick Start

### 零依赖预览（推荐先看这个）
直接用浏览器打开 `demo/index.html`（或任意静态服务器托管 `demo/` 目录），无需安装任何东西。

### 完整工程
```bash
# 前端
cd frontend && npm install && npm run dev

# 后端
cd backend
pip install -r requirements.txt
cp .env.example .env   # 填入你的 LLM_API_KEY
uvicorn app.main:app --reload
```

## URL 参数化演示

```
demo/index.html?video=https://cdn.example.com/brand.mp4&brand=YourBrand&autoclose=true
```

| 参数 | 说明 |
|---|---|
| `video` | 15s 样片 MP4 地址（未提供时使用 Canvas 动态生成的品牌动效） |
| `brand` | 品牌名（渲染到 Canvas 样片与 HUD） |
| `autoclose` | 进入后自动关门播放 |

## 项目结构 / Structure

```
elevad/
├── demo/        # 零依赖 CDN 版 3D 场景（快速迭代/演示用）
├── frontend/    # Vite + Vue3 完整工程
├── backend/     # FastAPI + RAG 管道
└── docs/        # PRD、演示剧本、面试叙事
```

## Roadmap

- [x] Phase 0: 项目骨架 + 零依赖 3D 电梯场景（轿厢/双开门/材质/交互）
- [ ] Phase 1: 关门动效 + VideoTexture 投影 + Canvas 动态样片生成
- [ ] Phase 2: AI Copilot（RAG 案例库 + 文案生成 + 策略输出）
- [ ] Phase 3: 全链路串联 + 安全加固（JWT/限流/Prompt注入防护）+ Docker 部署
- [ ] Phase 4: 压测报告 + 演示视频

## License

MIT
