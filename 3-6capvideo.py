import cv2

cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 640, 480)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("video", frame)

        key = cv2.waitKey(1)
        if(key & 0xFF == ord("q")):
            break
    else:
        print("false!")
        break


cap.release()
cv2.destroyAllWindows()