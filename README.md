# Object Detection with YOLOv11

## Overview
This project focuses on object detection using YOLOv11. The model is trained to detect various objects, including animals, household items, and food categories. The dataset was annotated using LabelImg, and the YOLO model was trained to identify multiple classes accurately.

## Features
- Object detection using YOLOv11
- Custom dataset annotation with LabelImg
- Detection of multiple object categories
- Model training and evaluation

## Detected Objects
The trained model can detect the following objects:
- Dog
- Person
- Cat
- TV
- Car
- Meatballs
- Marinara Sauce
- Tomato Soup
- Chicken Noodle Soup
- French Onion Soup
- Chicken Breast
- Ribs
- Pulled Pork
- Hamburger
- Cavity
- Horse
- Teddy Bear
- Cellphone

## Tools & Technologies Used
- **YOLOv11** for object detection
- **LabelImg** for annotation
- **Python** for scripting and model training
- **OpenCV** for image processing
- **TensorFlow/PyTorch** (depending on the implementation)

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/object-detection-yolov11.git
   cd object-detection-yolov11
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Annotate images using LabelImg and save in YOLO format.
4. Train the YOLOv11 model using the collected dataset:
   ```sh
   python train.py --data dataset.yaml --epochs 50 --batch-size 16
   ```
5. Run inference on test images:
   ```sh
   python detect.py --source test_images/ --weights best.pt --conf 0.5
   ```

## Results
- Model trained with YOLOv11 achieved high accuracy in detecting objects.
- Real-time object detection with minimal latency.

## Future Improvements
- Improve model accuracy with a larger dataset.
- Fine-tune hyperparameters for better performance.
- Deploy the model using Flask or FastAPI for real-time inference.

## Acknowledgments
- YOLO community for continuous improvements.
- Open-source contributors for LabelImg and dataset preparation.

## License
This project is licensed under the MIT License.
