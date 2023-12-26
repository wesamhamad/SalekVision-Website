from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from PIL import Image
from io import BytesIO
import base64

model = YOLO("bestR.pt")
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict-webcam", methods=["POST"])
def predict_webcam():
    data = request.json
    base64_image = data["image"].split(',')[1]
    image_data = base64.b64decode(base64_image)

    with open("test.jpg", "wb") as f:
        f.write(image_data)
    image = Image.open("test.jpg")

    detections = model(image)
    all_detection_classes = []

    for detection in detections:
        # Access the class IDs from the boxes attribute
        detected_class_ids = detection.boxes.cls.tolist()
        # Convert class IDs to names
        detected_class_names = [
            detection.names[int(class_id)] for class_id in detected_class_ids]
        all_detection_classes.extend(detected_class_names)

    inference_speed = str(
        sum(result.speed["inference"] for result in detections) / len(detections)) + "ms"

    return jsonify({
        'class_names': all_detection_classes,
        'inference_speed': inference_speed
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5050)
