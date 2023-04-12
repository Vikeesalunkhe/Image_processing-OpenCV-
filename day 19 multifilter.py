import cv2
import numpy as np

img=cv2.imread(r"C:\Users\VikeeDada\Downloads\nature image opencv.jpg")
img=cv2.resize(img,(500,500))

#gray image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#BRIGHTNESS
brightness=cv2.convertScaleAbs(img,beta=80)

#sharpness
kernel = np.array([[-1,-1,-1],[-1,9.5,-1],[-1,-1,-1]])
sharpness=cv2.filter2D(img,-1,kernel)

#pencilsketch
sk_gray,sk_color=cv2.pencilSketch(img,sigma_s=60,sigma_r=0.07,shade_factor=0.1)

#HDR EFFECT
hdr=cv2.detailEnhance(img,sigma_s=150,sigma_r=0.15)

#invert filter
inv=cv2.bitwise_not(img)





cv2.imshow("original",img)
cv2.imshow("gray_image",gray)
#cv2.imshow("brightness",brightness)
#cv2.imshow("sharpness",sharpness)
cv2.imshow("pencilsketch",pencilsketch)
cv2.imshow("HDR",hdr)
cv2.imshow("invert_image",inv)
