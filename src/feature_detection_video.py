import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
while(True):
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(image=gray,scaleFactor=1.3, minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, pt1=(x,y), pt2=(x+w,y+h),color=(0,0,255),thickness=5)
        cv2.putText(frame,text='face',org=(x,y),fontFace=cv2.FONT_HERSHEY_PLAIN, color=(0,255,0),thickness=5,
                fontScale=3)
        
        roi_gray = gray[y:y+h,x:x+h]
        roi_color = frame[y:y+h,x:x+h]

        eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.2,minNeighbors=2)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,pt1=(ex,ey),pt2=(ex+ew,ey+eh),color=(0,0,255),thickness=3)
            cv2.putText(roi_color,text='eye',org=(ex,ey),fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.2,color=(0,255,0),thickness=4)
        
        

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cap.release()
        break
cv2.destroyAllWindows()
  