import socket

# pip install PySocks
import socks
import requests



a = requests.get("http://checkip.amazonaws.com").text
print (a)

# Tor使用9150端口为默认的socks端口
socks.set_default_proxy(socks.SOCKS5, "jp2-sta115.67548.pw", 45137, password='4ENyCSFLpAAbT3d')
socket.socket = socks.socksocket
# 获取这次抓取使用的IP地址
a = requests.get("http://checkip.amazonaws.com").text

print (a)
