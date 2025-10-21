from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(1)
model = YOLO("yolo11n.pt")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    print("Frame shape:", type(frame), frame.shape)

    results = model(frame)

    for result in results:
        annotated_frame = result.plot()

    cv2.imshow("YOLOv11 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()