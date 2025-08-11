# VideoAnalytics-ModelBenchmarking

## Description
This repository contains datasets, scripts, and results for the paper:
**"Performance Comparison of Object Detection Models for Video Analytics Under Varying Video Quality"**.

The repository includes:
- **Video datasets** in three quality categories (High, Medium, Low)
- **Ground truth annotations** in COCO-compatible format
- **FFmpeg encoding scripts** to reproduce video quality variations
- **Inference scripts** for Fast R-CNN, EfficientDet, YOLOv5, YOLOv8, and DETR
- **Evaluation scripts** to compute Bitrate (Mbps), PSNR (dB), and Accuracy

---

## Video Quality Categories
The dataset is classified into three video quality categories based on encoding parameters.

| Category       | Resolution   | Frame Rate | Entropy Coding | Motion Estimation   | CRF  | Preset     | Quality Level | File Size | Encoding Speed |
|----------------|--------------|------------|----------------|---------------------|------|------------|--------------|-----------|----------------|
| **High**       | 1920x1080    | 30 fps     | CABAC          | UMH + subq 10       | 18   | slow       | High         | Small     | Slow           |
| **Medium**     | 1280x720     | 25 fps     | CABAC          | Hex                 | 28   | medium     | Medium       | Medium    | Medium         |
| **Low**        | 640x360      | 15 fps     | CAVLC          | Zero                | 35   | ultrafast  | Low          | Large     | Very Fast      |

---

## Video Dataset Access
The videos are hosted on YouTube for easy access and demonstration.

- **High Quality**: [Watch on YouTube](https://youtu.be/zkM6UASHdPQ)
- **Medium Quality**: [Watch on YouTube](https://youtu.be/ArZpNYl9fr8)
- **Low Quality**: [Watch on YouTube](https://youtu.be/YZ0vb7mOdf8)

---

## Environment Setup

This project was implemented and tested under the following environment:

- **conda version**: 23.1.0  
- **Python**: 3.9.23 (main experiments), Python 3.8 (DETR environment)  
- **PyTorch** with CUDA 11.8 (`conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia`)  
- **Detectron2**: `git clone https://github.com/facebookresearch/detectron2.git`  
- **DETR**: `git clone https://github.com/facebookresearch/detr.git`  
- **GPU**: NVIDIA GeForce RTX 5080  
- **CUDA Version**: 12.9  
- **Operating System**: Ubuntu 24.04.2 LTS  
- **FFmpeg**: version 4.3, built with gcc 7.3.0 (crosstool-NG 1.23.0.449-a04d0)

---

## Encoding Script
The `convert_quality.py` script is used to generate the High, Medium, and Low quality videos from a single input video using FFmpeg:contentReference[oaicite:1]{index=1}.

Example usage:
```bash
python scripts/encoding/convert_quality.py
