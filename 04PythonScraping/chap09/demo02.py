#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url = 'http://w3school.com.cn/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
xx = soup.find('div',id='d1').h2.text
print (xx)
















