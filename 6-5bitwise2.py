import cv2
import numpy as np

img = np.zeros ((200,200), np.uint8)
img2 = np.zeros ((200,200), np.uint8)
img[20:120, 20:120] = 114
img2 [80:180, 80:180]= 255

img3 = cv2.bitwise_and(img, img2)
cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()