import cv2
from ultralytics import YOLO
import threading
import time

class VisionEngine(threading.Thread):
    def __init__(self, model_path="yolov8n.pt", callback=None):
        super().__init__()
        self.model = YOLO(model_path)
        self.callback = callback
        self.running = True
        self.daemon = True

    def run(self):
        cap = cv2.VideoCapture(0)
        while self.running:
            ret, frame = cap.read()
            if not ret:
                time.sleep(0.1)
                continue

            results = self.model(frame, verbose=False)
            
            # Extract detections
            detections = []
            for r in results:
                for box in r.boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    label = self.model.names[cls]
                    detections.append({
                        "label": label,
                        "confidence": conf,
                        "box": box.xyxy[0].tolist()
                    })

            if self.callback and detections:
                self.callback(detections)

            # Control frame rate for telemetry
            time.sleep(0.1)

        cap.release()

    def stop(self):
        self.running = False
