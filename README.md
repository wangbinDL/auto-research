# Auto Research — AI 科研闭环系统

> 让 AI 自动做 CV 科研（目标检测/语义分割），录制完整决策轨迹，训练下一代 Qwen 模型。

## 项目目标

用 3 个月时间，4 人团队 + 64 GPU，搭建 Auto Research 闭环系统：
- **Agent 自动做科研**：观察→假设→修改→实验→分析→迭代
- **录制决策轨迹**：每一步想了什么、改了什么、结果如何
- **训练 Qwen 模型**：用轨迹数据让模型学会自主科研，接近 Codex/Claude Code 水平

## 系统架构

```
吴凡(M1+M2)          何天尧(M3+M4)         栗维鸿(M5+M6)        负责人(M7)
实验底座              Agent 核心             数据炼金              质量门禁
                          │                      │                    │
experiment_spec.yaml ◄────┤                      │                    │
experiment_result.json ───►│                      │                    │
                          │── trajectory.jsonl ──►│                    │
                          │                      │── model_manifest ──►│
```

## 技术栈（2026.05 验证）

| 领域 | 工具 |
|------|------|
| 目标检测 | Ultralytics YOLO26 |
| 语义分割 | HuggingFace Transformers + Mask2Former |
| Agent 编排 | LangGraph v0.3 |
| 搜索策略 | AIDE 式树搜索 |
| LLM 训练 | ms-swift v4 + DeepSpeed ZeRO-3 |
| 实验追踪 | Weights & Biases |
| 分布式 | FSDP2 / DeepSpeed ZeRO-3 |

## 目录结构

```
auto-research/
├── agent/                  # M3+M4 Agent 核心 (Owner: 何天尧)
│   ├── schemas/            # trajectory_schema.json
│   ├── tools/              # Agent 工具接口
│   └── tests/
├── cv_platform/            # M1+M2 实验平台 (Owner: 吴凡)
│   ├── docker/             # Dockerfile
│   ├── slurm/              # Slurm 模板
│   ├── configs/            # Ultralytics/HF 配置
│   ├── scripts/            # 训练评测脚本
│   └── tests/
├── data_training/          # M5+M6 质检与训练 (Owner: 栗维鸿)
│   ├── filtering/          # 质检过滤规则
│   ├── reward/             # reward 重算/建模
│   ├── conversion/         # SFT/DPO 格式转换
│   ├── training/           # ms-swift v4 配置
│   └── tests/
├── benchmark/              # M7 评测 (Owner: 负责人)
│   ├── tasks/              # 固定任务集
│   ├── evaluator/          # 自动评测脚本
│   └── reports/
├── interfaces/             # 跨模块接口定义（全员维护）
├── mocks/                  # Mock 数据（解耦开发用）
├── docs/                   # 项目文档
├── scripts/                # 工具脚本
└── tests/integration/      # 集成测试
```

## 快速开始

```bash
# 1. 克隆项目
git clone <repo-url> && cd auto-research

# 2. 搭建环境（吴凡负责的基础镜像）
cd cv_platform/docker && docker build -t cv-agent-base .

# 3. 验证 baseline
cd ../scripts && bash run_detection_baseline.sh
```

## 四个跨人接口

| 接口 | 方向 | 用途 |
|------|------|------|
| `interfaces/experiment_spec.yaml` | Agent → CV平台 | 提交实验请求 |
| `interfaces/experiment_result.json` | CV平台 → Agent | 返回实验结果 |
| `interfaces/trajectory.jsonl` | Agent → 质检训练 | 轨迹数据流转 |
| `interfaces/model_manifest.yaml` | 训练 → Benchmark | 模型元信息 |

## 里程碑

| 编号 | 时间 | 目标 |
|------|------|------|
| M1 | W2 (6/6) | 环境就绪 + baseline 跑通 + Schema v0.1 |
| M2 | W4 (6/20) | 接口冻结 + 单任务闭环跑通 |
| M3 | W6 (7/4) | 真实轨迹流通 + 首批 50 条质检 |
| M4 | W8 (7/18) | Benchmark 冻结 + 训练集 ≥200 条 |
| M5 | W10 (8/1) | Qwen v1 训练完成 + 首轮评测 |
| M6 | W12 (8/15) | 最终验收：CV 科研能力接近 Codex 水平 |

## 团队

| 成员 | 模块 | 职责 |
|------|------|------|
| 何天尧 | M3+M4 | Agent 编排引擎 + 轨迹采集存储 |
| 吴凡 | M1+M2 | GPU 环境 + CV 基线平台 |
| 栗维鸿 | M5+M6 | 数据质检 + 模型训练 Pipeline |
| 负责人 | M7 | Benchmark 评测 + 方向决策 |

## 协作规范

- **每日异步 standup**：做了/卡了/明天（文字，3 句话）
- **每周五 Demo**：各模块最新版联调，只看能跑的系统
- **每 2 周 Sprint Review**：里程碑检查 + 下阶段规划
- **接口变更**：任何 field 变动需 4 人确认

## License

Internal use only — 基模数据团队
