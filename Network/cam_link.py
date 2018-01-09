# coding=utf-8
from Configuration.config import *
import os
ip = get_ip()
#print(ip)

def cam_link():
    cmd = "ping -c 1 %s" % ip
    response = os.system(cmd)  # 如果连接成功会返回0
    if response == 0:
        print("HIKCam is connected !")
        return 0
    else:
        print("HIKCam is not connected !")
        return 1

if __name__ == "__main__":
    cam_link()


