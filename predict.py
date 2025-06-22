from ultralytics import YOLO
import sys

model = YOLO('yolo11n.pt')
source = sys.argv[1] if len(sys.argv) > 1 else '0'
model.predict(source=source, show=True, save=True, conf=0.6)