#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup

def test():
    url = 'http://tiku.gaokao.com/search/type0/光合作用'
    response = requests.get(url)
    # 1 get web page data
    # print(response.content) # print(response.text)
    web_page = response.content
    # 2 phrase web page data
    soup = BeautifulSoup(web_page, 'html.parser')  # 使用python默认的解析器
    # 解析搜索结果
    articals = soup.find_all('article', class_="result-item")
    for ar in articals:
        if '简介' in ar.get_text():
            for hr in ar.find_all('a'):
                print(hr.get('href'))




if __name__=='__main__':
    test()