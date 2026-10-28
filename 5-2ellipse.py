import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)


cv2.ellipse(img, (250, 240), 
            (100, 50), 30, 60, 270, 
            (0, 0, 255), 33)
cv2.ellipse(img, (300, 240), 
            (100, 50), 150, 90, 300, 
            (0, 0, 255), 33)
    



cv2.imshow("5-2ellipse", img)
while cv2.waitKey(1) != ord("q"):
    pass
cv2.destroyAllWindows()