from ultralytics import YOLO

# Load a model
# model = YOLO("yolo11n.yaml")  # build a new model from YAML
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
# # model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="dataset.yaml", epochs=100, imgsz=640, workers = 0, batch = 8)
# Display the results
# # results[0].show() 

# # Extract and print metrics
# precision = results.results_dict['metrics/precision']
# recall = results.results_dict['metrics/recall']
# f1_score = 2 * (precision * recall) / (precision + recall)
# map50 = results.results_dict['metrics/mAP_0.5']

# print(f"Precision: {precision:.4f}")
# print(f"Recall: {recall:.4f}")
# print(f"F1 Score: {f1_score:.4f}")
# print(f"mAP@50: {map50:.4f}")