import cv2 as cv

# reading images
img =  cv.imread('photos\\cat_large.jpg')
cv.imshow('Cat',img)

# reading videos
capture = cv.VideoCapture('videos//dog.mp4')
while True:
    isTrue, frame = capture.read()

    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('a'):
        break

capture.release()
cv.destroyAllWindows()