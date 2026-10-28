import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)


cv2.ellipse(img, (320, 240), 
            (100, 50), 0, 0, 360, 
            (255, 0, 0), 2)





cv2.imshow("5-2ellipse", img)
cv2.waitKey(0)
cv2.destroyAllWindows()