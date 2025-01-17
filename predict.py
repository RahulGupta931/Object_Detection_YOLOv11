from ultralytics import YOLO

model = YOLO('yolo11n.pt')
model.predict(source='0', show=True, save=True)