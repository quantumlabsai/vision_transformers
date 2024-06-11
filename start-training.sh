#!/bin/bash
python tools/train_detector.py --epochs 10 --batch 2 --data data/aduana.yaml --model detr_resnet50 --name detr_resnet50 --imgsz 300 
