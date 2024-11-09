import cv2 as cv
import numpy as np

img = cv.imread('photos//park.jpg')
cv.imshow('image',img)

#Average Blur
average = cv.blur(img,(3,3)) #greater the number more will be the blur
cv.imshow('averge_blur',average)

#Gausian Blur
gausian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gausian_blur',gausian)

#Median Blur
median = cv.medianBlur(img,3)
cv.imshow('median_blur',median)

#Bilateral Blur
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)