import cv2
import numpy as np

img=cv2.imread("pilu.jpg")
#cv2.imshow("original" ,img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_image" ,gray)
           
t
