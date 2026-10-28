import cv2
import numpy as np


curshape = 0
startpos = (0, 0)



def onMouse(event, x, y, flags, userdata):
    # print(f"event:{event}, x:{x}, y:{y}, flags:{flags}, userdata:{userdata}")
    
    global curshape, startpos
    if event & cv2.EVENT_LBUTTONDOWN:
        startpos = (x, y)
    elif event & cv2.EVENT_LBUTTONUP:
        if curshape == 0:
            cv2.line(img, startpos, (x, y), (0, 255, 0))
        elif curshape == 1:
            cv2.rectangle(img, startpos, (x, y), (0, 255, 0))
        elif curshape == 2:
            a = (x - startpos[0])
            b = (y - startpos[1])
            radius = int(np.sqrt(a**2 + b**2))

            cv2.circle(img, (x, y), radius, (0, 255, 0))




cv2.namedWindow("5-6实战", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("5-6实战", onMouse, "123")

img = np.zeros((480, 640, 3), np.uint8)


while True:
    cv2.imshow("5-6实战", img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break
    elif key & 0xFF == ord("l"):
        curshape = 0
    elif key & 0xFF == ord("r"):
        curshape = 1
    elif key & 0xFF == ord("c"):
        curshape = 2

cv2.waitKey(0)
cv2.destroyAllWindows()