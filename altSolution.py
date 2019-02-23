import cv2

left = cv2.VideoCapture(0)
right = cv2.VideoCapture(1)

while True:
    if not (left.grab() and right.grab()):
        print("No more frames")
        break

    _, leftFrame = left.retrieve()
    _, rightFrame = right.retrieve()

    #cv2.imshow('left', leftFrame)
    #cv2.imshow('right', rightFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(leftFrame,rightFrame)
    cv2.imshow(disparity,'gray')

left.release()
right.release()
cv2.destroyAllWindows()