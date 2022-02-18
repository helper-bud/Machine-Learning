import cv2

#> importing image
img = cv2.imread("res/lena.jpg")# for reading the image
cv2.imshow("Output",img) # for showing the image
cv2.waitKey(2000) # will delay the time. 0 means infinity. 2000 means 2s



# importing video
cap = cv2.VideoCapture("res/video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(2) & 0xFF == ord('q'): # wait key adds the delay and pressing q exit the video
        break


# importing webcoam

cap = cv2.VideoCapture(0)
cap.set(3,640) # cap.set(width id,width)
cap.set(4,480) # (height id, height)
cap.set(10,100) #(brightness id, brightness)
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(2) & 0xFF == ord('q'): # wait key adds the delay and pressing q exit the video
        break
