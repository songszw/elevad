# ElevAd 学习计划 —— 用项目本身学会 JD 的全部技术栈

> 原则：不做脱离项目的"看教程"。每个知识点都在 elevad 里有一个对应的地方等你动手改。
> 节奏：6 周，每天 1-1.5 小时。每周一个主题，周末做"毕业检验"。
> 分工：Minis 搭骨架/踩坑/写好注释版代码 → 你读懂 + 亲手改一个指定任务 → 讲给 Minis 听（费曼检验）。

## 第 1 周：Python 后端基础 → FastAPI（对应JD：后端API/微服务）
- Day1-2：Python 复习（函数/类/字典列表推导/venv）—— 只补这四样，别通读教程
- Day3-4：FastAPI：跑起 `backend/app/main.py`，读懂每个装饰器；用浏览器打开 `/docs` 玩自动生成的交互文档
- Day5：pydantic 模型：给 ProposalRequest 加一个 `audience` 字段并验证
- Day6：自己写一个 `/api/hello` 接口（带查询参数）
- Day7：检验 = 用 curl 调通自己写的接口，向 Minis 复述"请求进来后发生了什么"
- 📚 资料：FastAPI 官方教程前 5 章（中文版 fastapi.tiangolo.com/zh）

## 第 2 周：LLM API + Prompt 工程（对应JD：大语言模型应用/Prompt Engineering）
- Day1-2：直调 GLM API（openai SDK，20行代码）：temperature/max_tokens/system prompt 是什么
- Day3：写 3 版 system prompt 生成广告文案，对比输出差异 —— 这就是 Prompt Engineering 的全部入门
- Day4-5：结构化输出（JSON mode）：让模型返回 {morning, afternoon} 两版文案
- Day6：函数调用（Function Calling）概念：让模型决定"该查案例库还是直接写文案"
- Day7：检验 = 把 GLM 生成的文案接到 3D 场景的 ?brand= 参数里看效果
- 📚 资料：GLM / OpenAI 官方文档的 quickstart + chat completions 两页，够了

## 第 3 周：RAG（对应JD：RAG架构/向量数据库/语义检索 —— 核心中的核心）
- Day1：概念课（Minis 讲）：embedding=把文字变坐标 → 相似度=坐标距离 → 检索=找最近的
- Day2：embedding API 实操：把 10 条案例各算一个向量，打印出来看
- Day3-4：手写迷你 RAG（50行）：案例入库 → 用户问题 → 检索 top3 → 拼进 prompt → 生成带引用的回答
- Day5：换 LangChain 重写同一功能（对比体会框架价值）
- Day6：切分（chunking）与调优：案例太长怎么办
- Day7：检验 = 关掉检索 vs 开着，对比回答质量，能说出为什么
- 📚 资料：LangChain RAG 教程（python.langchain.com），只看 RAG 一节

## 第 4 周：前端串联（对应JD：前端 React/Vue 任一 + 交互）
- Day1-2：Vue3 单文件组件：读懂 frontend/src/App.vue 每一行
- Day3：表单绑定：把"品牌/预算/目标"三输入框做出来，POST 到 /api/propose
- Day4-5：流式输出（streaming）：打字机效果展示 AI 生成过程 —— 面试高频题
- Day6：把返回的文案渲染进 3D 场景
- Day7：检验 = 手机上走通全链路

## 第 5 周：部署 + 安全（对应JD：Docker/K8s/CI + OWASP）
- Day1-2：Docker：读懂 backend/Dockerfile，本地 build+run
- Day3：docker compose 把前后端一起拉起来
- Day4：安全三件套实操：给 API 加 JWT 登录、加限流（slowapi）、做一次 Prompt 注入攻击自己的接口再防住
- Day5：GitHub Actions：push 自动跑测试
- Day6：K8s 概念课（Minis 讲）：Pod/Deployment/Service，读懂仓库里的 k8s manifests
- Day7：检验 = 部署到 Oracle 服务器，手机公网访问

## 第 6 周：Agent + 压测 + 总复习（对应JD：Agent + 高并发 + 面试准备）
- Day1-2：Agent：让模型自主决定调用顺序（查案例→生成→组装H5）
- Day3：locust 压测自己的 API，出一页报告
- Day4-5：面试题自测（Minis 出题30道，覆盖JD每个关键词）
- Day6：录制 3 分钟演示视频
- Day7：模拟面试（Minis 扮演面试官，按 FDE JD 逐条追问）

## 分工红线
- **你亲手做的**：每周 Day5-7 的动手任务（这些就是面试时"你做过什么"的答案）
- **Minis 做的**：骨架、踩坑、代码注释版、24小时答疑、每周检验出题
- 规则：Minis 写的每个文件，你至少要能指出"改哪一行能改变什么"，做不到就问

## 现在的起点
你今天就能做的第一件事（30分钟）：打开 `backend/app/main.py`，数一数有几个函数、每个函数头上有什么装饰器，把不懂的名词发给 Minis。这就开始了。
