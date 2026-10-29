import cv2
import numpy as np

img = cv2.imread("tb.png")



img2 = cv2.flip(img, 0)
cv2.imshow("7-2flip2", img2)

img3 = cv2.flip(img, 1)
cv2.imshow("7-2flip3", img3)

img4 = cv2.flip(img, -1)
cv2.imshow("7-2flip4", img4)

while cv2.waitKey(1) != ord("q"):
    pass


cv2.destroyAllWindows()