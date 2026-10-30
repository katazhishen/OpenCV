import cv2

cv2.namedWindow("local_video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("local_video", 640, 360)



cap = cv2.VideoCapture("车辆识别/test.mp4")

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"w:{w}")
print(f"h:{h}")
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"fps:{fps}")


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("local_video", frame)
    cv2.resizeWindow("local_video", 640, 360)

    key = cv2.waitKey(int(1000 / fps))
    if key & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()