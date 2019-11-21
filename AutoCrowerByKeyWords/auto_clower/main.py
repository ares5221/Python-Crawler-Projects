#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from docx import Document
import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import time
import os
import http.cookiejar
import urllib.parse
import urllib.error
import subprocess
import sqlite3
import win32crypt
from win32com import client as wc
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import shutil

def download(url):
    # chrome_options = Options()
    # prefs = {'download.default_directory': 'G:/Download/'}
    # chrome_options.add_experimental_option('prefs', prefs)
    # driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="G:/Download/AutoCrowerByKeyWords/data/drive/chromedriver.exe")
    driver = webdriver.Chrome(executable_path="G:/Download/AutoCrowerByKeyWords/data/drive/chromedriver.exe")
    driver.maximize_window()
    driver.set_page_load_timeout(5)
    ss = driver.get(url)
    # print(driver.page_source)  # 打印网页源代码
    time.sleep(1)
    label_list = driver.find_elements_by_link_text("下载")
    for item in label_list:
        item.click()
    # response = urllib.request.urlopen(url).read()
    # soup = BeautifulSoup(response, 'html.parser')  # 使用python默认的解析器
    # last = soup.find('a', class_='last')
    # pagenum = 1
    # try:
    #     pagenum = int(last.get_text().strip()[3:].strip()) + 1
    #     if int(last.get_text().strip()[3:].strip()) > 100:
    #         pagenum = 101
    # except:
    #     ''


def save_file(kw):
    #修改文件保存路径，及文件格式 由于无法读取doc，需要转换为docx
    base_save_path = r'C:/Users/12261/Downloads/'
    new_save_path = 'G:/Download/AutoCrowerByKeyWords/data/download_path/'
    newpath = new_save_path + kw + '/source/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for fname in os.listdir(base_save_path):
        if fname[-4:] == '.ini':
            continue
        oldname = base_save_path + fname
        newname = newpath + '/' + fname
        if not os.path.exists(newname):
            # os.rename(oldname, newname)
            shutil.move(oldname,newname)
        else:
            print(fname,' 该文件已经下载')


def file_classifier(kw):
    base_dir = './../data/download_path/'
    curr_dir = os.path.join(base_dir, kw)
    if not os.path.exists(os.path.join(curr_dir, '试题')):
        os.makedirs(os.path.join(curr_dir, '试题'))
    if not os.path.exists(os.path.join(curr_dir, '资料')):
        os.makedirs(os.path.join(curr_dir, '资料'))
    if not os.path.exists(os.path.join(curr_dir, '课件')):
        os.makedirs(os.path.join(curr_dir, '课件'))
    print('生成分类文件夹')
    for fname in os.listdir(curr_dir):
        if (fname[0] == '~' or fname[0] == '.'):
            continue
        curr_file_name = os.path.join(curr_dir,fname)
        if not os.path.isdir(curr_file_name):#仅处理文件，不关心文件夹
            # print(fname)
            # print(curr_file_name)
            source_type = text_content_analysis(curr_file_name)
            if source_type == '试题':
                newname = os.path.join(os.path.join(curr_dir, '试题'), fname)
                shutil.move(curr_file_name, newname)
            if source_type == '资料':
                newname = os.path.join(os.path.join(curr_dir, '资料'), fname)
                shutil.move(curr_file_name, newname)
            if source_type == '课件':
                newname = os.path.join(os.path.join(curr_dir, '课件'), fname)
                shutil.move(curr_file_name, newname)


def text_content_analysis(file_path):
    sp = os.path.split(file_path)
    abs_path = sp[0]
    file_name = sp[1]
    if file_name[-5:] == '.docx':
        # print(abs_path, 'WWWWWWWWWWWWWWWW', file_name)
        document = Document(file_path)  # 打开docx文件
        full_text = []
        for paragraph in document.paragraphs:
            full_text.append(paragraph.text)
        # print(file_name,full_text)
        if '试题' in file_name or ('答题表' in full_text and '班级' in full_text and '姓名' in full_text):
            return '试题'
        if '练习' in file_name or '同步练习' in full_text or '基础练习' in full_text or '资料' in file_name:
            return '资料'
        if '课件' in file_name or '笔记' in full_text or '专题' in file_name or '笔记' in file_name:
            return '课件'



def formater_file_name(kw):
    base_dir = r"G:\Download\AutoCrowerByKeyWords\data/download_path/"# 这个地方好像不支持相对路径，以及需要加r
    new_dir = r"G:\Download\AutoCrowerByKeyWords\data\download_path"
    curr_dir = os.path.join(os.path.join(base_dir, kw),'source')
    save_dir = os.path.join(new_dir, kw)
    for fname in os.listdir(curr_dir):
        if (fname[0] == '~' or fname[0] == '.'):
            continue
        curr_file_name = os.path.join(curr_dir,fname)
        if fname[-4:] == '.doc':
            word = wc.Dispatch('Word.Application')
            doc = word.Documents.Open(curr_file_name)
            newname = save_dir + '/' + fname[:-4] + '.docx'
            # print(curr_file_name)
            # print(newname)
            # print(fname,'ssssss')
            doc.SaveAs(newname, 16)
            doc.Close()




def main():
    key_words = ['光合作用', '圆锥曲线方程', '作用力']
    base_url_list = ['http://tiku.gaokao.com/search/type0/']
    # download
    for kw in key_words:
        for url_item in base_url_list:
            url = url_item + kw
            download(url)
        time.sleep(3)
        save_file(kw)
        time.sleep(3)
        formater_file_name(kw)
        file_classifier(kw)



if __name__=='__main__':
    # main()
    # save_file('haha')
    file_classifier('圆锥曲线方程')