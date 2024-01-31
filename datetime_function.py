import cv2
import datetime

##############for img
'''img = cv2.imread("apple_img.jpg")
img = cv2.resize(img , (500,500))

date_data = "Date:" +str(datetime.datetime.now())
img = cv2.putText(img , date_data ,(45,56) ,cv2.FONT_HERSHEY_TRIPLEX, 1, (1,223,4) ,1 ,cv2.LINE_AA)
cv2.imshow("date_time_img" , img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#################for capture_video

cap = cv2.VideoCapture(0)
print(cap)

while cap.isOpened():
    ret , frame = cap.read()
    if ret == True:
        text = "Date :" +str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_COMPLEX
        frame = cv2.putText(frame , text ,(56,78) ,font ,1, (23,255,66) ,3 ,cv2.LINE_AA)
        cv2.imshow("date_time_video" ,frame)
        k = cv2.waitKey(25)
        if k == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()'''

####################for memory_video

cap = cv2.VideoCapture("nature_video.mp4")
print(cap)

font = cv2.FONT_HERSHEY_TRIPLEX
text = "Date Time" +str(datetime.datetime.now())

while cap.isOpened():
    ret ,frame = cap.read()
    if ret == True:
        frame = cv2.putText(frame , text ,(23,56) ,font ,1 ,(222,45,67) ,1 ,cv2.LINE_AA)
        cv2.imshow("date_time_video" , frame)
        k = cv2.waitKey(25)
        if k == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
