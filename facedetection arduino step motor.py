import numpy as np
import cv2
import serial


ser = serial.Serial('COM3', 9600)
print (ser.portstr)
ser.write((b'\x10'))
cap = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier('C:/Users/eglardo/Downloads/haarcascade_frontalface_default.xml')

while (cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE,minSize=(60, 60), maxSize=None)


    if len(faces) > 0:

        ser.write((b'\x01'))
        print("Pessoa detectada!")
        print("Motor Girando") 

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x - 10, y - 20), (x + w + 10, y + h + 10), (0, 0, 255), 2)
            roi_gray = frame[y-15:y + h+10, x-10:x + w+10]
            cv2.putText(frame, "VINICIUS", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255)) 

        cv2.imshow("Do bit Ao Byte", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ser.write((b'\x10'))
cap.release()
cv2.destroyAllWindows()
