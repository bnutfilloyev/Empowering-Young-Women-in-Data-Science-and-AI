from ultralytics import YOLO
from ultralytics import settings

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

settings.update({"runs_dir": "/Users/bnutfilloyev/Developer/lesson/Module-5-Data-Cleaning-Preparation/medical-pills"})


# Train the model
results = model.train(data="medical-pills.yaml", epochs=100, imgsz=640)