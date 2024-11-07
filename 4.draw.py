import cv2 as cv
import numpy as np

#Blank Image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank_img',blank)

#paint the image with certain color
blank[:] = 0, 255, 0
cv.imshow('green_img',blank)

#paint certain portion of the image
blank[200:300 , 300:400] = 0,0,255
cv.imshow("red_box",blank)

#draw rectangles
cv.rectangle(blank, (0,0),(250,250),(0,0,255),thickness=cv.FILLED ) #cv.FILLED == -1
cv.imshow('rectangle_img',blank)

#draw circles
cv.circle(blank,(250,250),(40),(0,0,250),thickness=3)
#the above 21th line can also be written as
# cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),(40),(0,0,250),thickness=3)
cv.imshow('circle',blank)

#draw lines
cv.line(blank, (0,100),(250,250),(255,255,255),thickness=3)
cv.imshow('Line',blank)

#write text on image
cv.putText(blank,'Hello', (400,400),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)
