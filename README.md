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
