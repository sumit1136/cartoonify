# import the opencv library
import cv2
import numpy as np
from skimage import io
# define a video capture object
vid = cv2.VideoCapture(0)

while True:

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame 1', frame)

    # frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # cv2.imshow('frame 2', frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame 2', gray)

    imgBlur = cv2.medianBlur(gray, 5)
    # cv2.imshow('frame 2', imgBlur)

    imgEdge = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # cv2.imshow('frame 2', imgEdge)

    colored = cv2.bilateralFilter(frame, 9, 250, 250)
    cartoon = cv2.bitwise_and(colored, colored, mask=imgEdge)
    cv2.imshow('frame 2', cartoon)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
