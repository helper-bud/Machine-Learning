import cv2 as cv
import numpy as np

img = cv.imread('res/lena.JPG') # Reading Images
cv.imshow("Shapes",img)

# 1. convertinge to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# 2. Blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # (3,3) is the kernal size and it has to be negative. Control the blur effect
cv.imshow('Blur', blur)

# 3. Edge casecade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# 4. dialate an image
dialated = cv.dilate(canny, (3,3), iterations= 1)
cv.imshow('Dialated', dialated)

# 5. Eroding image
eroded = cv.erode(dialated, (3,3), iterations= 1)
cv.imshow('Eroded', eroded)

# 6. resizing
resize = cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', resize)

# 7. cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
