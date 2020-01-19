#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests

link = "http://www.santostang.com/"
proxies = {'http':'http://xxx.xxx.xxx.xxx:xxxx'}
response = requests.get(link, proxies=proxies)