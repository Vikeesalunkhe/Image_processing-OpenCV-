import cv2

img = cv2.imread("apple_img.jpg")
img = cv2.resize(img , (500,500))
cv2.imshow("Original_img ", img)
cv2.waitKey(0)
