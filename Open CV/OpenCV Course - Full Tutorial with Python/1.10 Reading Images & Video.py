import cv2
import cv2 as cv

'''
img = cv.imread('res/shapes.JPG') # Reading Images
cv.imshow("Shapes",img)
cv.waitKey(0)
'''

capture = cv.VideoCapture('res/video.mp4') # 0 means webcame, 1 means camera connected your computer

while True:
    isTrue, frame = capture.read() # capture.read() plays the video frame by frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release() 
cv.destroyAllWindows() # after the video is over it destroy all the window
cv.waitKey(0)
