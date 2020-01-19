#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
import os

g_adsl_account = {"name": "adsl",
                  "username": "...",
                  "password": "..."}


class Adsl(object):
    # __init__ : name: adsl名称
    def __init__(self):
        self.name = g_adsl_account["name"]
        self.username = g_adsl_account["username"]
        self.password = g_adsl_account["password"]

    # connect : 宽带拨号
    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        os.system(cmd_str)
        time.sleep(5)

    # disconnect : 断开宽带连接
    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        os.system(cmd_str)
        time.sleep(5)

    # reconnect : 重新进行拨号
    def reconnect(self):
        self.disconnect()
        self.connect()


if __name__ == '__main__':
    A = Adsl()
    A.reconnect()