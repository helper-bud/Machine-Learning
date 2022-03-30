import cv2 as cv
import numpy as np

img = cv.imread('res/lena.JPG') # Reading Images
#cv.imshow("Lena",img)

'''
contours are useful tools when you get into shape analysis and object detection 
and recognition
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
'''
countours is essentially a python list of all the co ordiantes of the coutours found in the image. 
RETR_LIST > return external contours.
RETR_TREE > all the hierarchical countours 
CHAIN_APPROX_SIMPLE > how you want to approxmate your contours.

'''
print(f'{len(contours)} contour(s) found!')

#cv.drawContours(blank, contours, -1, (0,0,255), 1)
#cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
