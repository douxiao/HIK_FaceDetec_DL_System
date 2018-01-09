# coding=utf-8
import os
import shlex
import subprocess

source = "rtsp://admin:520douxiao@192.168.199.64/Streaming/Channels/1"
cam_save_dir = "/data/视频/HIK_cam"
if not os.path.exists(cam_save_dir):  # 如果保存文件路径不存在就创建一个
    os.makedirs(cam_save_dir)

cmd = "ping -c 1 192.168.199.64"
args = shlex.split(cmd)
try:
    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("baidu server is up!")
except subprocess.CalledProcessError:
    print("Failed to get ping.")

    # cam = cv2.VideoCapture(source)
