import cv2
import numpy as np

img=cv2.imread("tilu.png")
font=cv2.FONT_HERSHEY_COMPLEX

cv2.putText(img,"vikee",(200,300),font,1,(0,255,255),2)


cv2.imshow("dark",img)


