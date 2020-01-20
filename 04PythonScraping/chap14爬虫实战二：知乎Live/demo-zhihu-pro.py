#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import json
import time
import random
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.zhihu_database_pro

live_id = '840520148518592512'


def get_audience(live_id):
    headers = {
        'Host': 'api.zhihu.com',
        'Origin': 'https://www.zhihu.com',
        'Referer': 'https://www.zhihu.com/lives',
        'authorization': 'oauth 8274ffb553d511e6a7fdacbc328e205d',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }
    link = 'https://api.zhihu.com/lives/' + live_id + '/members?limit=10&offset=0'

    is_end = False
    while not is_end:
        r = requests.get(link, headers=headers)
        html = r.text
        decodejson = json.loads(html)
        decodejson['live_id'] = live_id
        db.live_audience.insert_one(decodejson)

        link = decodejson['paging']['next']
        is_end = decodejson['paging']['is_end']
        time.sleep(random.randint(2, 3) + random.random())


# get_audience(live_id)

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.zhihu_database

for each_page in db.live.find():
    for each in each_page['data']:
        live_id = each['live']['id']
        print (live_id)
        get_audience(live_id)