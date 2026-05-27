#!/bin/bash
# 检测 Baseline 快速验证脚本
# Owner: 吴凡 (M1)
# 用途: 验证 Ultralytics YOLO26 环境是否正常

set -euo pipefail

echo "=== Auto Research — Detection Baseline ==="
echo "Framework: Ultralytics YOLO26"
echo "Dataset: COCO128 (验证用小数据集)"
echo ""

# 检查环境
python -c "import ultralytics; print(f'Ultralytics version: {ultralytics.__version__}')"
python -c "import torch; print(f'PyTorch version: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"

# 运行最小训练
echo ""
echo "Starting YOLO26-N training on COCO128 (5 epochs)..."
yolo detect train \
    model=yolo26n.pt \
    data=coco128.yaml \
    epochs=5 \
    imgsz=640 \
    batch=16 \
    project=/tmp/auto_research_baseline \
    name=yolo26n_coco128 \
    exist_ok=True

echo ""
echo "=== Baseline Complete ==="
echo "Results: /tmp/auto_research_baseline/yolo26n_coco128/"
