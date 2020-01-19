#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url = 'http://w3school.com.cn/'
r = requests.get(url)
# r.encoding = 'gb2312'
soup = BeautifulSoup(r.text, "lxml")
xx = soup.find('div',id='d1').h2.text
print (xx)

print(r.encoding)
import chardet
after_gzip = r.content
print ('解压后字符串的编码为',chardet.detect(after_gzip))
print (after_gzip.decode('GB2312'))













