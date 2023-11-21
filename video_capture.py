#capture video in your path location or img name
import cv2

#for User input img
#data = input("enter your video path or name.mp4 :")

#cap = cv2.VideoCapture(data)
cap = cv2.VideoCapture(r"nature_video.mp4")
print(cap)

while True:
    ret , frame = cap.read()
    frame = cv2.resize(frame , (500,250))      #frame resize
    cv2.imshow("frame" ,frame)

# press "q" to close output windows (destroyallwindos)
    k = cv2.waitKey(25)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
