import cv2

img = cv2.imread("apple_img.jpg")
img = cv2.resize(img , (500,500))
gray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)     #cv2.cvtColor : gray img
cv2.imshow("Original_img",img)
cv2.imshow("Gray_img" , gray)
cv2.waitKey(0)




