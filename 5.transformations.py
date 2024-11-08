import cv2 as cv
import numpy as np

img = cv.imread('photos//park.jpg')
cv.imshow('park',img)

#translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0]) #img.shape[0] = height, img.shape[1] = width
    return cv.warpAffine(img,transMat,dimensions)

# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down

translated = translate(img,-100,-100)
cv.imshow('translated',translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow('rotated_img',rotated)

#Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#Flipping
flip = cv.flip(img,1)
cv.imshow('flip',flip)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)