#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import json


def single_page_comment(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers=headers)
    # 获取 json 的 string
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']

    for eachone in comment_list:
        message = eachone['content']
        print(message)

for page in range(1, 11):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery1124015286285666718946_1579060476901&limit=10&offset="
    offset = str(page)
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1579060476909"
    link = link1 + offset + link2
    single_page_comment(link)