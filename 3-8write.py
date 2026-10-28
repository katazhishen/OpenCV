import cv2


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vw = cv2.VideoWriter("./out.mp4", fourcc, 25, (1280, 720))

# 创建窗口
cv2.namedWindow("local_video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("local_video", 640, 480)



cap = cv2.VideoCapture(0)

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"w:{w}")
print(f"h:{h}")
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"fps:{fps}")


while True:
    ret, frame = cap.read()
    if not ret:
        print("视频结束")
        break


    cv2.imshow("local_video", frame)

    vw.write(frame)

    key = cv2.waitKey(int(1000 / fps))
    if key & 0xFF == ord("q"):
        break


cap.release()
vw.release()
cv2.destroyAllWindows()