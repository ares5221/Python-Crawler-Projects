#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# pip install pymongo
import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.blog_database
collection = db.blog

link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers= headers)

soup = BeautifulSoup(r.text, "lxml")
title_list = soup.find_all("h1", class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.text.strip()
    post = {"url": url,
         "title": title,
         "date": datetime.datetime.utcnow()}
    collection.insert_one(post)