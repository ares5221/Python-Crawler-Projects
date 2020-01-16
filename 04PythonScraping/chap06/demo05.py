#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='scraping', charset="utf8")
cur = conn.cursor()

link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
title_list = soup.find_all("h1", class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.text.strip()
    cur.execute("INSERT INTO urls (url, content) VALUES (%s, %s)", (url, title))

cur.close()
conn.commit()
conn.close()