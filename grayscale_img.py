import cv2

#Original img
img1 = cv2.imread("apple_img.jpg",1)      #1 : default parameter (original_img)
img1 = cv2.resize(img1 ,(500,500))    #width , height
cv2.imshow("original_img",img1)

#Gray_scale_img
img2 = cv2.imread("apple_img.jpg", 0)     #0 : gray_img
img2 = cv2.resize(img2,(500,500))q
cv2.imshow("grayscale_img" ,img2)

#Unchanged_img
img3 = cv2.imread("apple_img.jpg", -1)     # -1 : extra colour img (bright)
img3 = cv2.resize(img3,(500,500))
cv2.imshow("unchanged_img" ,img3)
cv2.waitKey(3000)                            #visualization control  (3000 = 3 second)
cv2.destroyAllWindows()

