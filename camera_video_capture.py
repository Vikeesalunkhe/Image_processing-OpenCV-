import cv2

#Now capture video from webcam or laptop camera

cap = cv2.VideoCapture(0)      #(0) : laptop camera , #(1) : external  camera (webcam)
print(cap)

while cap.isOpened():
    ret  , frame = cap.read()
    if ret == True :
        frame = cv2.resize(frame , (500,250))
        cv2.imshow("Now capture video" , frame)

        k = cv2.waitKey(1)
        if k == ord("q"):        #press "q" to exit
            break

cap.release()
cv2.destroyAllWindows()
