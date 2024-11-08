import cv2 as cv
import numpy as np

img = cv.imread('photos//cats.jpg')
cv.imshow('cats',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(img,125,175)
cv.imshow('canny',canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

contourss = cv.drawContours(blank, contours, -1, (0,0,255),thickness=1)
cv.imshow('contours_drawn',contourss)

cv.waitKey(0)