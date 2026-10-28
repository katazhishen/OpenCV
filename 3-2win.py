import cv2

cv2.namedWindow("win", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("win", 640, 480)


cv2.imshow("win", 0)
key = cv2.waitKey(0)
if(key == 'q'):
    exit()

cv2.destroyAllWindows()
