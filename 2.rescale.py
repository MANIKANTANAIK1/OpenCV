import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('cat',img)

def rescaleFrame(frame,scale=0.75):
    # This method is useful for images,Videos and Live_videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width,height):
    #This method is useful only for Live_Videos
    capture.set(3,width)
    capture.set(4,height)

resized_image = rescaleFrame(img)
cv.imshow('image',resized_image)

capture = cv.VideoCapture('videos//dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=.2)
    cv.imshow('resized_video', frame_resized)
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('a'):
        break

capture.release()
cv.destroyAllWindows()