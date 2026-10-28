import cv2

cv2.namedWindow("3-10", cv2.WINDOW_NORMAL)


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("3-10", frame)
    
    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()