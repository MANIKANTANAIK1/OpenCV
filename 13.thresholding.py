import cv2 as cv
import numpy as np

img = cv.imread('photos//park.jpg')
cv.imshow('image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Threshold_inverse',thresh_inv)

#adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive Thresholding',adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('adaptive Thresholding',adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.ADAPTIVE_THRESH_GAUSSIAN_C,11,9)
cv.imshow('adaptive_gausian Thresholding',adaptive_thresh)



cv.waitKey(0)