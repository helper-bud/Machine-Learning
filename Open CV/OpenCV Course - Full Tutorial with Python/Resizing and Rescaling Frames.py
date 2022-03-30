# resizing videos


import cv2
import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('res/video.mp4') # 0 means webcame, 1 means camera connected your computer

while True:
    isTrue, frame = capture.read() # capture.read() plays the video frame by frame

    frame_resize = rescaleFrame(frame,scale=0.2 )

    cv.imshow('Video', frame)
    cv.imshow("Video resized",frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows() # after the video is over it destroy all the window
cv2.waitKey(0)
____________________________________________________________________________________




