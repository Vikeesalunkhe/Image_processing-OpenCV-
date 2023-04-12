import cv2
import numpy as np


img=cv2.imread(r"C:\Users\VikeeDada\Downloads\cv road car.webp")
gray=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)

_,threah=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

cv2.imshow("gray_image",gray)
cv2.imshow("binary_img",thresh)
