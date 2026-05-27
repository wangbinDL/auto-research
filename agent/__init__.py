"""
Agent 核心模块 — 科研闭环编排引擎 + 轨迹采集
Owner: 何天尧 (M3+M4)

职责:
- 基于 LangGraph v0.3 构建科研 Agent 状态机
- 实现 observe → hypothesize → plan → execute → analyze → reflect 循环
- 采集并存储决策轨迹 (trajectory.jsonl)
- 调用 CV 平台接口提交/查询实验
"""
