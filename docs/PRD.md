# ElevAd PRD（合并版）

## 定位
「媒仓提效 Copilot」= Tikin-3D（脸）+ AI Copilot（脑）
服务对象：梯影/媒仓的销售与投放顾问。
核心叙事：销售输入三句话 → 客户在手机上看到自己的广告在电梯里跑起来。

## 核心链路
```
输入: brand + budget + goal(三句话)
  → [AI层] RAG检索案例库 → 策略摘要 + 分时段文案 + 预算分配
  → [3D层] Canvas动态样片 → 实时投到3D电梯门(VideoTexture)
  → 输出: 可微信转发的沉浸式提案H5 (URL参数化, 底部"找顾问聊聊")
```

## Phase 计划
- P0 骨架: 仓库/CI/零依赖3D场景(轿厢+双开门+拉丝材质+交互) ← 当前
- P1 3D完整: 关门阻尼动效 + 投影渐显 + 品牌Canvas样片 + 微信兼容(autoplay引导/首触解锁)
- P2 AI层: 知识库构建(梯影案例/行业CPM基准) → FAISS → LangChain RAG → GLM-4生成
- P3 串联+安全: JWT / slowapi限流 / Prompt注入防护 / Docker Compose / GH Actions
- P4 压测+交付: locust压测报告 / 3分钟演示视频 / 敲门材料

## URL参数规范
?video=<mp4>&brand=<品牌名>&autoclose=true

## 安全要求(对齐FDE JD)
- OWASP: 输入校验(pydantic), API限流, JWT, CORS白名单
- Prompt注入: 用户输入与系统提示词隔离, 输出过滤
- 密钥: 全部环境变量, .gitignore已排除

## 演示剧本(敲门用, 3分钟)
1. 0:00-0:20 问题: 梯媒销售最大卡点="客户看不见效果"
2. 0:20-1:20 演示: 三句话输入 → 策略+文案生成 → 3D电梯里广告跑起来
3. 1:20-2:00 对标: 媒仓AI智投 vs 本工具(成交前 vs 成交后环节互补)
4. 2:00-3:00 价值: 40个投放顾问×每周省4小时 + 技术栈全对齐FDE岗位
