#!/bin/bash
#SBATCH --job-name=${EXPERIMENT_ID}
#SBATCH --output=/runs/${EXPERIMENT_ID}/slurm_%j.log
#SBATCH --error=/runs/${EXPERIMENT_ID}/slurm_%j.err
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gres=gpu:${GPU_COUNT}
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=${MAX_HOURS}:00:00

# Auto Research — Slurm 任务模板
# 由 CV 平台根据 experiment_spec 动态填充变量后提交

set -euo pipefail

echo "========================================="
echo "Experiment: ${EXPERIMENT_ID}"
echo "Task: ${TASK_TYPE}"
echo "Framework: ${FRAMEWORK}"
echo "GPUs: ${GPU_COUNT}"
echo "Node: $(hostname)"
echo "Started: $(date -Iseconds)"
echo "========================================="

# 激活环境
source /opt/conda/etc/profile.d/conda.sh
conda activate cv-agent

# 设置分布式训练环境变量
export MASTER_PORT=$(shuf -i 20000-30000 -n 1)
export WANDB_PROJECT="auto-research"
export WANDB_RUN_ID="${EXPERIMENT_ID}"

cd /workspace

# 根据框架选择执行方式
if [ "${FRAMEWORK}" = "ultralytics" ]; then
    python cv_platform/scripts/run_detection.py \
        --config "${CONFIG_PATH}" \
        --work-dir "/runs/${EXPERIMENT_ID}" \
        --seed ${SEED}
elif [ "${FRAMEWORK}" = "huggingface" ]; then
    torchrun --nproc_per_node=${GPU_COUNT} \
        cv_platform/scripts/run_segmentation.py \
        --config "${CONFIG_PATH}" \
        --work-dir "/runs/${EXPERIMENT_ID}" \
        --seed ${SEED}
fi

echo "Finished: $(date -Iseconds)"
