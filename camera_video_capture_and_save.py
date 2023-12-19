#Now capture video from webcam and save into memory

import cv2

cap = cv2.VideoCapture(0)        #(0)  laptop camera or (1) for external camera
print(cap)

#save into memory
#video formates DIVX , XVID , MJPG , WMV1 , WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")    #(*"XVID") = video format

#it cintains 4 parameter : path/name , codec ,fps , size ,
output = cv2.VideoWriter("C:\\output.avi" , fourcc , 20.0, (500,250))

while cap.isOpened():
    ret , frame  = cap.read()
    if ret == True :
        #frame = cv2.resize(frame , (500,250))
        #gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("gray video" , gray)
        cv2.imshow("now captured video" ,frame)
        output.write(fourcc)

        k = cv2.waitKey(1)
        if k == ord("q"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()
