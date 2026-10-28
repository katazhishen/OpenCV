import cv2
import numpy as np


cv2.namedWindow("trackbar", cv2.WINDOW_NORMAL)


def callback(type, pos):
    print(f"type:{type}, pos:{pos}")

cv2.createTrackbar("R", "trackbar", 0, 255, lambda pos: callback("R", pos))
cv2.createTrackbar("G", "trackbar", 0, 255, lambda pos: callback("G", pos))
cv2.createTrackbar("B", "trackbar", 0, 255, lambda pos: callback("B", pos))


img = np.zeros((480, 640, 3), np.uint8)

while True:
    cv2.imshow("trackbar", img)

    r = cv2.getTrackbarPos("R", "trackbar")
    g = cv2.getTrackbarPos("G", "trackbar")
    b = cv2.getTrackbarPos("B", "trackbar")
    img[:] = [b, g, r]

    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()