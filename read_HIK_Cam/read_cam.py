# coding=utf-8
import cv2
from Configuration.config import *  # 引入配置文件包

source = get_url()

cam = cv2.VideoCapture(source)

while (True):
    # get a frame
    ret, frame = cam.read()
    # show a frame
    cv2.imshow("window", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# 释放摄像头对象和窗口
cam.release()
cv2.destroyAllWindows()
