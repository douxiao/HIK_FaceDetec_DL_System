# coding=utf-8
import configparser

config = configparser.ConfigParser()
config.read("config.ini")  # 读取配置文件中的配置信息
user = config.get("accountConf", "user")
password = config.get("accountConf", "password")
host = config.get("ipConf", "host")


def get_rtsp():
    # 海康威视摄像头的RSTP地址
    # 海康威视摄像头采用的是RTSP协议 RTSP 实时串流协议(Real time stream protocol,RTSP)
    # 是一种网络应用协议，专为娱乐和通信系统使用，以控制流媒体服务器。
    rtsp = "rtsp://%s:%s@%s/Streaming/Channels/1" % (user, password, host)
    return rtsp


def get_ip():
    return host



if __name__ == "__main__":
    get_rtsp()
    get_ip()