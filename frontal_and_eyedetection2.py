#import packages 
import cv2 as cv 
import numpy as np

#resize the window
def rescaleframe(frame,scale= 0.75):
    width = int(frame.shape[1]*0.5)
    height = int(frame.shape[0]*0.5)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

face_frontal = cv.CascadeClassifier('haar_frontal.xml')
frontal_eye = cv.CascadeClassifier('haar_frontaleye.xml')

#access the camera 
capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    resized_vid = rescaleframe(frame)
    gray = cv.cvtColor(resized_vid,cv.COLOR_BGR2GRAY)

    faces_rect = face_frontal.detectMultiScale(gray,scaleFactor= 1.1,minNeighbors=3)
    eyes_rect = frontal_eye.detectMultiScale(gray,scaleFactor= 1.1,minNeighbors=3)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(resized_vid,(x,y),(x+w,y+h),(255,0,0),3)
        roi_gray = gray[x:x+w,y:y+h]
        roi_color = resized_vid[x:x+w,y:y+h]

    for (x,y,w,h) in eyes_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv.imshow('detection_cam',resized_vid)


    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture.realease()
cv.destroyAllWindows()


