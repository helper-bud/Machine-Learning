import cv2
import  numpy as np
# basic function

# > importing image
img = cv2.imread("res/lena.jpg")# for reading the image

kernal = np.ones((5,5), np.uint8) # 1st> size of the matix, 2nd> type of object.uint8[unsigned integer of 8bits]

# > converting into grayScale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# converts image in different color spaces

# > blurring image
imgBlur = cv2.GaussianBlur(img,(7,7),0)

imgCanny = cv2.Canny(img,100,100)


imgDialation = cv2.dilate(imgCanny,kernal,iterations= 5) # above we defined the kernal , then iteration will maximize the edge border

imgEroded = cv2.erode(imgDialation,kernal, iterations= 1)

cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)

'''
Edge Detector:
The Canny edge detector is an edge detection operator 
that uses a multi-stage algorithm to detect a wide range of edges in images. 

dialoute : to detect edge more properly
Dilation adds pixels to the boundaries of objects in an image, while erosion removes pixels on object boundaries.
To apply a morphological filter to images in Python using OpenCV, use the cv2 dilate() method. 
The dilate() method takes two inputs in which one is our input image; 
the second is called the structuring element or kernel, which decides the nature of the operation. 
Image dilation Increases the object area.

erotion:
Dilation adds pixels to the boundaries of objects in an image, 
while erosion removes pixels on object boundaries. 
The number of pixels added or removed from the objects in an image depends on the size 
and shape of the structuring element used to process the image.
'''

