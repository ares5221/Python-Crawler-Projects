#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import datetime

import time


def get_page(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers=headers)
    html = r.content
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_data(post_list):
    data_list = []
    curr_list = post_list[0].find_all('li')
    for post in curr_list:
        title = post.find('div', class_='titlelink box').text.strip()
        post_link = post.find('div', class_='titlelink box').a['href']
        post_link = "https://bbs.hupu.com" + post_link

        author = post.find('div', class_='author box').a.text.strip()
        author_page = post.find('div', class_='author box').a['href']
        start_date = post.find('div', class_='author box').contents[5].text.strip()

        reply_view = post.find('span', class_='ansour box').text.strip()
        reply = reply_view.split('/')[0].strip()
        view = reply_view.split('/')[1].strip()

        reply_time = post.find('div', class_='endreply box').a.text.strip()
        last_reply = post.find('div', class_='endreply box').span.text.strip()

        if ':' in reply_time:
            date_time = str(datetime.date.today()) + ' ' + reply_time
            date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M')
        else:
            date_time = datetime.datetime.strptime('2017-' + reply_time, '%Y-%m-%d').date()
        data_list.append([title, post_link, author, author_page, start_date, reply, view, last_reply, date_time])
    return data_list


class MongoAPI(object):
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conn = MongoClient(host=self.db_ip, port=self.db_port)
        self.db = self.conn[self.db_name]
        self.table = self.db[self.table_name]

    def get_one(self, query):
        return self.table.find_one(query, projection={"_id": False})

    def get_all(self, query):
        return self.table.find(query)

    def add(self, kv_dict):
        return self.table.insert(kv_dict)

    def delete(self, query):
        return self.table.delete_many(query)

    def check_exist(self, query):
        ret = self.table.find_one(query)
        return ret != None

    # 如果没有会新建
    def update(self, query, kv_dict):
        self.table.update_one(query, {
            '$set': kv_dict
        }, upsert=True)


hupu_post = MongoAPI("localhost", 27017, "hupu", "post")
for i in range(1, 2):
    link = "https://bbs.hupu.com/bxj-" + str(i)
    soup = get_page(link)

    post_list = soup.find_all('ul', class_='for-list')
    data_list = get_data(post_list)
    for each in data_list:
        hupu_post.update({"post_link": each[1]}, {"title": each[0],
                                                  "post_link": each[1],
                                                  "author": each[2],
                                                  "author_page": each[3],
                                                  "start_date": str(each[4]),
                                                  "reply": each[5],
                                                  "view": each[6],
                                                  "last_reply": each[7],
                                                  "last_reply_time": str(each[8])})

    time.sleep(3)
    print('第', i, '页获取完成，休息3秒')
