import cv2
import numpy as np

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img", 800, 800)

img = cv2.imread("tb.png")
img = cv2.bitwise_not(img)
cv2.imshow("img", img)





cv2.waitKey(0)
cv2.destroyAllWindows()