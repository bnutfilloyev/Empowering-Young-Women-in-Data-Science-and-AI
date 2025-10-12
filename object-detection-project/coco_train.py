from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on COCO8
results = model.train(data="coco8.yaml", epochs=20, imgsz=640)