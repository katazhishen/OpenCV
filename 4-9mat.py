import cv2
import numpy as np

img = cv2.imread("tb.png")

img2 = img

img3 = img.copy()

img[10:100,10:100] = [255,0,0]

cv2.imshow("4-9mat", img)
cv2.imshow("4-9mat2", img2)
cv2.imshow("4-9mat3", img3)

cv2.waitKey(0)

cv2.destroyAllWindows()