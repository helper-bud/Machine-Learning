import cv2
import  numpy as np

def empty(a):
    pass
# joining image
img = cv2.imread("res/lambo.png")


# detection of color in the image
imgHSV  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # HSV or Hue Saturation Value is used to separate image luminance from color information

'''
Hues are made up of the three primary colors (red, blue, and yellow) and the three secondary colors (orange, green, and violet) that appear in the color wheel or color circle. When you refer to hue, you are referring to its pure color, or the visible spectrum of basic colors that can be seen in a rainbow
'''
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
'''
before
cv2.createTrackbar("Hue Min","TrackBars", 0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars", 179,179,empty)

cv2.createTrackbar("Sat Min","TrackBars", 0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars", 255,255,empty)

cv2.createTrackbar("Val Min","TrackBars", 0,255,empty)
cv2.createTrackbar("Val Max","TrackBars", 255,255,empty)
'''

# after getting the resutl
cv2.createTrackbar("Hue Min","TrackBars", 0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars", 21,179,empty)

cv2.createTrackbar("Sat Min","TrackBars", 110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars", 255,255,empty)

cv2.createTrackbar("Val Min","TrackBars", 159,255,empty)
cv2.createTrackbar("Val Max","TrackBars", 255,255,empty)


'''
getTrackbarPos() is Function in Python OpenCV that returns the current position of the specified trackbar. It takes two arguments. The first is for the trackbar name and the second one is the window name which is the parent of the trackbar. Returns the trackbar position
'''
''''''
while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min,s_max,v_min,v_max)
    # we get the result and set it in the trackbar

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    # we got the new value and now we will out desired color
    imgResult = cv2.bitwise_and(
        img,img,mask=mask
    )

    cv2.imshow("Image",imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("masked", imgResult)
    cv2.waitKey(1)
