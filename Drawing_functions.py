import cv2
import numpy as np

img = cv2.imread("apple_img.jpg")
img = cv2.resize(img , (500,500))

#draw_blank_img
#img = np.zeros([512, 512, 3], np.uint8)*255   #for black blank screen
#img = np.ones([512, 512, 3], np.uint8)*255     #for white blank screen


#line accept 5 parameter (img , starting, ending, color, thikness)
img = cv2.line(img , (0,0) , (200,200) , (255,6,77) , 4)

#arrowed line accept also 5 parameter (img , starting , ending, color, thikness )
img = cv2.arrowedLine(img, (0,125) , (255,255) , (235,0,244) , 6)

#rectangle - accept paramete (img , start_co , radius , color , thikness)
img = cv2.rectangle(img  , (345,12) , (431,56) , (34,78,45) ,-1)   #thikness (+value) = out line  ,(-value) : blank

#circle - accept parameter (img , start_co , end_co, color , thikness)
cv2.circle(img , (233,344) ,45, (234,56,0) ,44)

font = cv2.FONT_ITALIC    #font type
#put text - accept parameter (img, text, start_co, font, fountsize ,color, thikness, linetype )
img = cv2.putText(img, "vikee", (23,456), font, 2, (45,34,2), 5, cv2.LINE_AA )

#ellipse accept(img, start_co, (length,height), color, thickness)
img = cv2.ellipse(img, (400,400), (100,50),0,0,180,155,5)

while True:
    cv2.imshow("drow_img" , img)
    k = cv2.waitKey(0)
    if k ==ord("q"):   #press "q" to exit
        break
cv2.destroyAllWindows()
