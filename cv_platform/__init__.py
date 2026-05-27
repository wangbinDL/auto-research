"""
CV 实验平台 — GPU 环境管理 + 训练/评测执行
Owner: 吴凡 (M1+M2)

职责:
- Docker 基础镜像构建与维护
- Slurm 任务调度模板
- Ultralytics YOLO26 检测训练 Pipeline
- HuggingFace Mask2Former 分割训练 Pipeline
- 接收 experiment_spec → 执行 → 返回 experiment_result
"""
