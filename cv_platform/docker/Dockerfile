# Auto Research — CV 实验平台基础镜像
# Owner: 吴凡 (M1)
# 用途: 提供统一的检测/分割训练环境

FROM nvidia/cuda:12.4-devel-ubuntu22.04

LABEL maintainer="wufan"
LABEL description="CV Agent Base Image — Ultralytics YOLO26 + HuggingFace Transformers"

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV TORCH_HOME=/cache/torch
ENV HF_HOME=/cache/huggingface

# 系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 python3.11-venv python3-pip \
    git wget curl \
    libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/bin/python3.11 /usr/bin/python && \
    ln -sf /usr/bin/python3.11 /usr/bin/python3

# Python 依赖
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 工作目录
WORKDIR /workspace

# 默认入口：训练脚本由 Slurm/docker run 指定
CMD ["python", "--version"]
