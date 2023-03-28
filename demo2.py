import cv2

img=cv2.imread("opencv car img.jpg")
img=cv2.resize(img,(500,500))
cv2.imshow("original",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_image" ,gray)
cv2.waitKey(0)
cv2.distroyAllWindow()
