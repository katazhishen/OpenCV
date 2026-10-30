import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

video_path = "车辆识别/test.mp4"
cap = cv2.VideoCapture(video_path)
print("是否打开成功：", cap.isOpened())

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


min_w = 90
min_h = 90

# 线高
line_high = 600

# 线的偏移
offset = 10

# 车辆数量
carno = 0

# 车辆列表
cars = []

# 计算矩形的中心坐标
def center(x, y, w, h):
    return (x + w // 2, y + h // 2)


# 形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 背景减除器 长时间不变的默认为背景
bgsubmog = cv2.createBackgroundSubtractorMOG2()

# 视频帧率
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"fps:{fps}")


while True:
    ret, frame = cap.read()
    if not ret:
        print("读取帧失败/视频结束")
        break

    # 灰度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 去噪
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    # 去背景
    mask = bgsubmog.apply(blur)
    # 腐蚀 去掉图中的小方块
    erode = cv2.erode(mask, kernel, iterations=1)
    # 膨胀 还原放大物体
    dilate = cv2.dilate(erode, kernel, iterations=3)
    # 闭运算 去掉物体内部的小方块
    close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    for i in range(4):
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)
    
    cnts, h = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame,(10, line_high), (width - 10, line_high), (255, 255, 0), 3)
    for cnt in cnts:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 对车辆的宽高进行筛选
        isValid = (w >= min_w and h >= min_h)
        if not isValid:
            continue

        cpoint = center(x, y, w, h)
        cars.append(cpoint)


        for (x, y) in cars:
            if((y < line_high + offset) and (y > line_high - offset)):
                carno += 1
                cars.remove((x, y))
                print(f"累计有{carno}辆车辆通过喵～")
                

    cv2.putText(frame, f"we have {carno} cars", (400, 500), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 160, 222), 4)
    cv2.imshow("车辆识别", frame)
    key = cv2.waitKey(int(1000 / fps)) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
