import cv2
from ultralytics import YOLO

model = YOLO('/Users/bnutfilloyev/Developer/lesson/Module-5-Data-Cleaning-Preparation/pill-counter/models/pill_detection_weight.pt')
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # resize to 640x640
    # frame = cv2.resize(frame, (640, 640))
    
    results = model(frame, verbose=False, conf=0.6)
    # for result in results:
    #     print(result.boxes)
    annotated = results[0].plot()
    num_pills = len(results[0].boxes)
    
    cv2.putText(annotated, f'Pills: {num_pills}', (10, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Pill Detection - Press Q to quit', annotated)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break