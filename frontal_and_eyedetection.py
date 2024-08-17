import cv2 as cv

def rescaleframe(frame, scale=0.75):
    # Rescale the frame to a smaller size by multiplying width and height by the given scale factor
    width = int(frame.shape[1] * scale)  # Calculate the new width based on the scale
    height = int(frame.shape[0] * scale) # Calculate the new height based on the scale
    dimensions = (width, height)         # Create a tuple with the new dimensions

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    # Resize the frame to the new dimensions using the INTER_AREA interpolation method, which is good for shrinking images

# Load the pre-trained Haar Cascade classifier for face detection
haar_cascade = cv.CascadeClassifier('haar_frontal.xml')
# Load the pre-trained Haar Cascade classifier for eye detection
haar_cascade_eye = cv.CascadeClassifier('haar_frontaleye.xml')

# Capture video from the default webcam (index 0)
capture = cv.VideoCapture(0)

while True:  # Continuously read frames from the webcam
    isTrue, frame = capture.read()  # Read a frame from the video capture object
    resized_vid = rescaleframe(frame)  # Rescale the frame to the specified size
    gray = cv.cvtColor(resized_vid, cv.COLOR_BGR2GRAY)  # Convert the resized frame to grayscale for detection
    
    # Detect faces in the grayscale frame
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    # Detect eyes in the grayscale frame
    eye_rect = haar_cascade_eye.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces_rect:
        cv.rectangle(resized_vid, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a green rectangle around the face
        roi_gray = gray[y:y + h, x:x + w]   # Region of interest in the grayscale image
        roi_color = resized_vid[y:y + h, x:x + w]  # Region of interest in the colored image
        
    # Draw rectangles around detected eyes
    for (x, y, w, h) in eye_rect:
        cv.rectangle(resized_vid, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a green rectangle around the eye
    
    # Display the video with detected faces and eyes
    cv.imshow('detect', resized_vid)

    # If the 'q' key is pressed, exit the loop and stop capturing video
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
capture.release()
cv.destroyAllWindows()

    
