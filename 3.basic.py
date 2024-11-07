import cv2 as cv

img = cv.imread('photos\\park.jpg')
cv.imshow('park',img)

#converting an image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur an image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#Dilatinf the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated',dilated)

#Eroding
eroded = cv.erode(dilated,(7,),iterations=3)
cv.imshow('eroded',eroded)

#resize an image
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#cropping
cropped = img[50:200 , 200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)