# Object Detection with YOLOv11 using Custom Dataset

## Overview
This project demonstrates how to train and evaluate an **Object Detection Model** using **YOLOv11** on a custom dataset annotated with **LabelImg**.

## Features
- Train **YOLOv11** on a custom dataset
- Annotate images using **LabelImg**
- Evaluate model performance using metrics like **mAP, Precision, and Recall**
- Deploy and test object detection on images and video streams

## Prerequisites
### **1. Install Dependencies**
```bash
pip install ultralytics opencv-python torch torchvision torchaudio matplotlib labelImg
```

### **2. Clone YOLOv11 Repository**
```bash
git clone https://github.com/ultralytics/ultralytics.git
cd ultralytics
```

### **3. Prepare the Dataset**
1. **Collect Images**: Gather images relevant to the detection task.
2. **Annotate with LabelImg**:
   - Install LabelImg:  
     ```bash
     pip install labelImg
     labelImg
     ```
   - Draw bounding boxes and save in **YOLO format** (`.txt` files).
3. **Organize the Dataset**:
   ```
   dataset/
   ├── train/
   │   ├── images/
   │   │   ├── img1.jpg
   │   │   ├── img2.jpg
   │   └── labels/
   │       ├── img1.txt
   │       ├── img2.txt
   ├── val/
   │   ├── images/
   │   └── labels/
   └── data.yaml
   ```

### **4. Train the Model**
```bash
yolo task=detect mode=train model=yolov11n.pt data=dataset/data.yaml epochs=50 imgsz=640
```

### **5. Evaluate Model Performance**
```bash
yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=dataset/data.yaml
```

### **6. Run Inference**
#### **On an Image**
```bash
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=path/to/image.jpg
```
#### **On a Video/Webcam**
```bash
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=0
```

## Model Performance Metrics
- **Precision & Recall**: Measures detection accuracy
- **mAP (Mean Average Precision)**: Evaluates the model’s ability to detect objects correctly

## Deployment
Convert the trained model for optimized inference:
```bash
yolo export model=runs/detect/train/weights/best.pt format=onnx
```

## Acknowledgments
- **Ultralytics** for YOLOv11
- **LabelImg** for annotation

## License
This project is open-source under the MIT License.
