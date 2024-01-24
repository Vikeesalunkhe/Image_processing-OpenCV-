import cv2

cap = cv2.VideoCapture("nature_video.mp4")
print(cap)

print("width : ",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("height : ",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret ,frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = "vikee"
        #puttext(img , teXT ,(x,y), font ,font_size ,colour ,thikness ,line_format )
        frame = cv2.putText(frame ,text ,(10,202) ,font ,1 ,(0,155,255), 1, cv2.LINE_AA)
        #frame = cv2.resize(frame ,(700,500))
        cv2.imshow("capture_video" , frame)

        k = cv2.waitKey(25)
        if k == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
