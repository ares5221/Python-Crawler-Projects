#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import requests
import wget
import time
from bs4 import BeautifulSoup


def download_with_requests(url, file_name):
    base_dir = './../test_docsavefile'
    save_path = os.path.join(base_dir, file_name)
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(save_path):
        ss = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(ss.content)
        print(file_name, ' 该文件下载完成 ', 'curr time----> :', curr_time)
    else:
        print(file_name, ' 文件已经存在 ', 'curr time----> :', curr_time)



def download_with_wget(file_name, url, key):
    base_dir = './../data_v2/source'
    save_dir = os.path.join(base_dir, key)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_name +='.doc' #todo 这里如果是其他文件会有问题，需要手动改后缀
    # filename = wget.detect_filename(url) + '.doc' # todo 自动获取文件名是一个id的格式，有问题待查
    save_path = os.path.join(save_dir, file_name)
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(save_path):
        filename = wget.download(url, out=save_path)
        print(file_name, ' 该文件下载完成 ', 'curr time----> :', curr_time)
    else:
        print(file_name, ' 文件已经存在 ', 'curr time----> :', curr_time)


def download_file_use_middle_website(search_key, titles, middle_websites):
    print(titles)
    download_website = []
    for curr_url in middle_websites:
        response = requests.get(curr_url)
        web_page = response.content
        soup = BeautifulSoup(web_page, 'html.parser')
        download_info = soup.find_all('a', class_="download lm10 op8")
        for dlw in download_info:
            # print(dlw.get('href'))
            download_website.append(dlw.get('href'))
    for index in range(len(titles)):
        # print(titles[index], download_website[index])
        download_with_wget(titles[index], download_website[index], search_key)




if __name__=='__main__':
    url = 'http://tiku.gaokao.com/download/type6/id7483'
    file_name = '高中生物必修1光合作用同步练习1.doc'
    download_with_requests(url, file_name)
    # download_with_wget(url, file_name)