import cv2
import cv2 as cv
import numpy as np

# blank image
blank = np.zeros((500,500,3), dtype= 'uint8') #(height,width, number of color channel )
cv.imshow("Blank Image code",blank)

# 1. paint the image at a certain colour

blank[:] = 0,255,0
cv2.imshow('Green', blank)

#2. for coloring certain portion of the image

blank[200:300, 300:400] = 0,0,255
cv2.imshow('Partically Colored Image', blank) # make sure your image has the same size

# 3. draw a rectangle
cv.rectangle(blank,(0,0), (250,250), (0,250,0), thickness= 2 ) #(image, point one, ponint two, color, thickness)
cv.imshow('Rectangle', blank)

# 4. if you want to fill up the color
cv.rectangle(blank,(0,0), (250,250), (0,250,0), thickness= cv.FILLED ) # thickness= cv.FILLED  / thickness = -1
cv.imshow(' Filled the Rectangle with green color', blank)

# 5. draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255), thickness=3) # (img, center, radius, color, thickness)
cv.imshow("circle in image", blank)

# 6. draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,255,255), thickness=3)# (img, starting point, ending ponint,  color, thicnkess)
cv.imshow("line in picture", blank)

#  7. Write text
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) #( image, text, orgin, font face, font scale, color, thickness )
cv.imshow("text in picture", blank)

cv.waitKey(0)
