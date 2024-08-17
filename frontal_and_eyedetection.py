import cv2 as cv

def rescaleframe(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions =(width,height)

    return cv.resize(frame,dimensions,interpolation =cv.INTER_AREA)

haar_cascade= cv.CascadeClassifier('haar_frontal.xml')
haar_cascade_eye= cv.CascadeClassifier('haar_frontaleye.xml')

capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    resized_vid =rescaleframe(frame)
    gray = cv.cvtColor(resized_vid,cv.COLOR_BGR2GRAY)
    # grey=cv.GaussianBlur(gray,(5,5),0)
    # cv.imshow("live video",resized_vid)
    faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    eye_rect = haar_cascade_eye.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(resized_vid,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray =gray[y:y+h,x:x+w]
        roi_color = resized_vid[y:y+h,x:x+w]
        # cv.putText(faces_rect,str('face'),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    for (x,y,w,h) in eye_rect:
        cv.rectangle(resized_vid,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('detect',resized_vid)


    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()

    