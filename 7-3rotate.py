import cv2
import numpy as np

img = cv2.imread("tb.png")

img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("7-3rotate2", img2)

img3 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("7-3rotate3", img3)

img4 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("7-3rotate4", img4)



while cv2.waitKey(1) != ord("q"):
    pass


cv2.destroyAllWindows()