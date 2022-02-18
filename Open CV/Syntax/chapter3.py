import cv2
import  numpy as np
# basic function

# > importing image
img = cv2.imread("res/lena.jpg")# for reading the image
print(img.shape) #> (512, 512, 3) (width, height, number of your channels)

image_resize = cv2.resize(img,(300,200)) #(which image,(width, height))
print(image_resize.shape) #> (200, 300, 3)

image_cropped = img[0:200, 200:500] #(height-> 0  to 200  , width -> 200 to 500)

cv2.imshow("img",img)
cv2.imshow("resize image",image_resize)
cv2.imshow("cropped image", image_cropped)
cv2.waitKey(0)
