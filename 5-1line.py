import cv2
import numpy as np

img = np.zeros((480,640,3), np.uint8)

cv2.line(img, (100,100), (200,200), 
         (0,255,0), 8, 4)

cv2.imshow("5-1line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()