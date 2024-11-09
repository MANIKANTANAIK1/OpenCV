import cv2 as cv
import numpy as np

img = cv.imread('photos//park.jpg')
cv.imshow('image',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#split an image to seperate colors
b,g,r = cv.split(img)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge b,g,r seperately on blank image
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

#merge all color channels in one image
merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

cv.waitKey(0)