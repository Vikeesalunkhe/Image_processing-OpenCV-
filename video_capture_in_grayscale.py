import cv2

cap = cv2.VideoCapture("nature_video.mp4")
print(cap)

while True:
    ret , frame = cap.read()
    frame = cv2.resize(frame , (500,250))
    gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original" , frame)
    cv2.imshow("Gray" ,gray)

    k = cv2.waitKey(25)        #25 : normal speed
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
