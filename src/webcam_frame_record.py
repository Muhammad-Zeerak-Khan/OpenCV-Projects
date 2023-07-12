import cv2

cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cap.read()
    cv2.imshow("Live Feed", frame)
    cv2.imwrite(f"webcam_data/Image_{count}.jpg", frame)
    count += 1
    if cv2.waitKey(1) & 0xFF== ord('q'):
        cap.release()
        break
cv2.destroyAllWindows()    