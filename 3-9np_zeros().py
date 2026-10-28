import cv2
import numpy as np

cv2.namedWindow("np", cv2.WINDOW_NORMAL)

img = np.zeros((360, 640, 3), np.uint8)
while True:
    cv2.imshow("np", img)

    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()
