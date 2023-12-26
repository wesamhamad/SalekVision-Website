from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor


model = YOLO("bestR.pt")

model.predict(source="0", show=True, conf=0.5)
