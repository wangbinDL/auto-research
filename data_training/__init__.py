"""
数据质检与模型训练 Pipeline
Owner: 栗维鸿 (M5+M6)

职责:
- 轨迹数据质检过滤（规则 + LLM-as-Judge）
- Reward 模型训练 / 重算
- SFT/DPO/GRPO 格式转换
- ms-swift v4 训练配置与执行
- 训练完成后生成 model_manifest
"""
