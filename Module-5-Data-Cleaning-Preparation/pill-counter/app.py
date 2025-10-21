import cv2
from ultralytics import YOLO

model = YOLO('models/pill_detection_weight.pt')
cap = cv2.VideoCapture(0)

frame_count = 0
pill_counts = []
counting = False

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    results = model(frame)
    annotated = results[0].plot()
    num_pills = len(results[0].boxes)
    
    if num_pills > 0 and not counting:
        counting = True
        frame_count = 0
        pill_counts = []
    
    if counting:
        pill_counts.append(num_pills)
        frame_count += 1
        cv2.putText(annotated, f'Counting: {frame_count}/20', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        if frame_count >= 20:
            avg_pills = int(sum(pill_counts) / len(pill_counts))
            cv2.putText(annotated, f'Final Count: {avg_pills}', (10, 110), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            counting = False
            frame_count = 0
            pill_counts = []

            
    cv2.putText(annotated, f'Pills: {num_pills}', (10, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Pill Detection - Press Q to quit', annotated)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
