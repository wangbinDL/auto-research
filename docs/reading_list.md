# Auto Research — 必读清单（2026.05 验证）

> CCG 三方调研（Claude + Codex/GPT-5.5 + Gemini），2026-05-27 整理

---

## 一、核心技术栈 Repos

| Repo | Stars | 最新版本 | 用途 |
|------|------:|---------|------|
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | ~33k | **v1.2.2** (2026-05-26) | Agent 编排骨架：有状态图、checkpoint、human-in-the-loop、失败恢复 |
| [WecoAI/aideml](https://github.com/WecoAI/aideml) | ~1.3k | v0.2.2 (2025-11) | AIDE 树搜索参考实现：代码生成→执行→metric 评估→剪枝 |
| [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | ~57k | **v8.4.56** (2026-05-27) | YOLO26 目标检测/分割/Pose/OBB，NMS-free + MuSGD |
| [modelscope/ms-swift](https://github.com/modelscope/ms-swift) | ~14k | **v4.2.2** (2026-05-24) | Qwen 系列训练：SFT/DPO/GRPO/量化/部署 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | ~161k | **v5.9.0** (2026-05-20) | Mask2Former 语义分割 + 模型 Hub 集成 |
| [facebookresearch/Mask2Former](https://github.com/facebookresearch/Mask2Former) | ~3.4k | **Archived** (2025-01) | 仅做架构参考，生产代码用 HF Transformers |

**注意：**
- LangGraph 当前是 v1.2.x，不是 v0.3（项目初始文档中的版本已过时）
- YOLO26 通过 `ultralytics` 包交付，不是独立 repo
- Mask2Former 原始仓库已归档，使用 HuggingFace 版本

---

## 二、自主科研 / 闭环 Agent Repos

| Repo | Stars | 活跃度 | 为什么必读 |
|------|------:|--------|-----------|
| [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | ~6.4k | 2025 末 | 完整科研闭环：构思→实验→写论文→审稿，Progressive Agentic Tree Search |
| [sjtu-sai-agents/EvoMaster](https://github.com/sjtu-sai-agents/EvoMaster) | ~180 | **Active 2026-05** | 2026 最接近我们系统：run-level 自进化、轨迹分析、技能生成、prompt overlay |
| [sjtu-sai-agents/ML-Master](https://github.com/sjtu-sai-agents/ML-Master) | ~407 | 2026-03 | 探索+推理架构+自适应记忆（已被 EvoMaster 取代，读设计即可） |
| [facebookresearch/aira-dojo](https://github.com/facebookresearch/aira-dojo) | ~148 | 2025-09 | AI 科研 Agent 框架：task/agent 抽象、隔离执行、Slurm 友好 |
| [facebookresearch/llm-speedrunner](https://github.com/facebookresearch/llm-speedrunner) | ~142 | 2025-10 | 评估 Agent 能否复现代码级科研提升（NanoGPT speedrun） |
| [openai/mle-bench](https://github.com/openai/mle-bench) | ~1.5k | 2026-04 | ML 工程 Agent 标准 benchmark（Kaggle 任务），评测参考 |

---

## 三、轨迹记录 / 实验观测 Repos

| Repo | Stars | 最新版本 | 用途 |
|------|------:|---------|------|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | ~28k | v3.175.0 (2026-05-21) | LLM 观测：traces/evals/prompt 管理/OpenTelemetry，录制 Agent 决策轨迹 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | ~9.9k | Active 2026-05 | AI 观测 + evaluation + 可重放 traces（Langfuse 备选） |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | ~26k | v3.12.0 (2026-05) | CV 实验 tracking：metrics/artifacts/model registry/checkpoints |
| [epsilla-cloud/clawtrace](https://github.com/epsilla-cloud/clawtrace) | ~37 | Active 2026-05 | 新兴轨迹录制：LLM calls/tool calls/sub-agent/token cost → TraceCards |

---

## 四、必读论文

### 4.1 自主科研 Agent

| 论文 | 作者 | 日期 | 链接 | 相关性 |
|------|------|------|------|--------|
| **The AI Scientist v2: Workshop-Level Automated Scientific Discovery** | Lu, Hu et al. (Sakana AI) | 2025-04 | [arXiv:2504.08066](https://arxiv.org/abs/2504.08066) | 最完整的 AI 科研闭环：构思→实验→论文→审稿，Progressive Agentic Tree Search |
| **AIDE: The Machine Learning Engineer Agent** | Jiang et al. (Weco AI) | 2025-02 | [arXiv:2502.13138](https://arxiv.org/abs/2502.13138) | 树搜索解空间探索 + metric-driven 剪枝，我们系统的搜索策略参考 |
| **The AI Scientist** (v1) | Lu et al. (Sakana AI) | 2024-08 | [arXiv:2408.06292](https://arxiv.org/abs/2408.06292) | 奠基工作：首次实现 idea→code→paper→review 全自动化 |
| **EvoMaster: Self-Evolving Scientific Agent** | SJTU-SAI | 2026 | [GitHub](https://github.com/sjtu-sai-agents/EvoMaster) | 运行级自进化 + 轨迹学习，最接近我们"用轨迹训练模型"的设计 |

### 4.2 Agentic 轨迹数据训练

| 论文 | 作者 | 日期 | 链接 | 相关性 |
|------|------|------|------|--------|
| **FireAct: Toward Language Agent Fine-tuning** | Chen et al. | 2023-10 | [arXiv:2310.05915](https://arxiv.org/abs/2310.05915) | 用多任务 agent 轨迹微调 LLM，证明 trajectory SFT 有效 |
| **Agent-FLAN: Designing Data and Methods of Effective Agent Tuning** | Chen et al. | 2024-03 | [arXiv:2403.12881](https://arxiv.org/abs/2403.12881) | 系统化 Agent 数据设计：负样本、幻觉过滤、分解训练 |
| **AgentTrek: Agent Trajectory Synthesis via Guiding Replay** | Zhang et al. | 2025 | [arXiv:2025](https://arxiv.org/) | 轨迹合成方法：guided replay 生成高质量训练轨迹 |
| **Agent Workflow Memory (AWM)** | Wang et al. | 2024 | [arXiv](https://arxiv.org/) | 从轨迹中提取可复用 workflow → 提升 Agent 泛化 |

### 4.3 奖励建模 / 研究质量评估

| 论文 | 作者 | 日期 | 链接 | 相关性 |
|------|------|------|------|--------|
| **LLM-as-Judge** (Zheng et al.) | LMSYS | 2023-06 | [arXiv:2306.05685](https://arxiv.org/abs/2306.05685) | 用 LLM 评判输出质量，我们的轨迹质检基础 |
| **GRPO: Group Relative Policy Optimization** | Shao et al. (DeepSeek) | 2024-02 | [arXiv:2402.03300](https://arxiv.org/abs/2402.03300) | 无需 critic 的 RLHF，ms-swift 已原生支持 |
| **Self-play for LLM Alignment** | Various | 2024-2025 | — | 强模型生成轨迹→弱模型执行→自动评分的数据飞轮 |

### 4.4 评测 Benchmark

| Benchmark | 用途 | 链接 |
|-----------|------|------|
| **MLE-bench** (OpenAI) | ML 工程 Agent 能力评估 | [GitHub](https://github.com/openai/mle-bench) |
| **SWE-bench Verified** | 软件工程 Agent (PR 修复) | [swe-bench.github.io](https://www.swebench.com/) |
| **GAIA** | 通用 AI 助手（多步推理+工具） | [huggingface.co/gaia-benchmark](https://huggingface.co/gaia-benchmark) |
| **τ-bench** | Agent 工具使用评估 | [GitHub](https://github.com/sierra-research/tau-bench) |
| **TheAgentCompany** | 长程企业任务 Agent | [theagentcompany.com](https://www.theagentcompany.com/) |

---

## 五、阅读优先级

**第一周必读（何天尧优先）：**
1. AI Scientist v2 论文 + 源码
2. AIDE 论文 + `aideml` 源码
3. EvoMaster 源码（最新 2026）
4. LangGraph v1.2 文档（注意不是 v0.3）

**第一周必读（栗维鸿优先）：**
1. FireAct + Agent-FLAN 论文
2. ms-swift v4 文档（SFT/DPO/GRPO 流程）
3. Langfuse 文档（轨迹录制格式）

**第一周必读（吴凡优先）：**
1. Ultralytics YOLO26 文档 + 配置
2. HF Transformers Mask2Former 教程
3. MLflow 实验追踪

---

## 六、版本修正记录

| 组件 | 项目文档中的版本 | 实际最新版本 | 备注 |
|------|-----------------|-------------|------|
| LangGraph | v0.3 | **v1.2.2** | 大版本升级，API 有变化 |
| Ultralytics | YOLO26 | v8.4.56 (含 YOLO26) | YOLO26 是 ultralytics 包的一部分 |
| ms-swift | v4 | v4.2.2 | 版本正确 |
| HF Transformers | — | v5.9.0 | — |
| Mask2Former | — | **Archived** | 用 HF 版本替代 |
