#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup   #从bs4这个库中导入BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers= headers)

soup = BeautifulSoup(r.text, "html.parser")   #使用BeautifulSoup解析这段代码
title = soup.find("h1", class_="post-title").a.text.strip()
print (title)

with open('title_test.txt', "a+", encoding='utf-8') as f:
    f.write(title)
    f.close()