# import cv2
# import numpy as np
# from ultralytics import YOLO


# class Camera(object):
#     def __init__(self):
#         # Open the webcam (change the index if needed)
#         self.cap = cv2.VideoCapture(0)
#         # Initialize the YOLO model with your weights file
#         self.model = YOLO("bestR.pt")

#     def __del__(self):
#         self.cap.release()

#     def detect_objects(self, frame):
#         results = self.model(frame)  # Perform object detection
#         # Extract relevant information (class, location, accuracy, speed) from results
#         if len(results.pred) > 0:
#             # Get the detected class
#             detection_info = results.names[results.pred[0][0][5]]
#         else:
#             detection_info = "No Object Detected"
#         return detection_info

#     def get_frame(self):
#         success, frame = self.cap.read()  # Read a frame from the webcam
#         if not success:
#             return None, None

#         detection_info = self.detect_objects(frame)

#         # Draw the detected class on the frame
#         cv2.putText(frame, f"Detected Object Class: {detection_info}", (
#             10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#         # Encode the frame in JPEG format
#         _, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()

#         return frame, detection_info
