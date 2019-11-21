# coding=utf8
import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import time
import string
import os
import http.cookiejar
import urllib.parse
import urllib.error
import subprocess
import sqlite3
import win32crypt
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pymysql

conn = pymysql.connect("localhost", "root", "1234", "21edu",use_unicode=True, charset="utf8")
cur = conn.cursor()
count=19186
kgtest=''

def get_chrome_cookies(url):
    conn = sqlite3.connect("Cookies")
    ret_dict = dict()
    for row in conn.execute("SELECT host_key, name, path, value, encrypted_value FROM cookies"):
        # if row[0] not in url:
        if row[0] != url:
            continue
        #print(row[0])
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        #print(ret[1].decode())
        ret_dict[row[1]] = ret[1].decode()
    conn.close()
    return ret_dict

def downloadDoc(get_url,filename):
    get_url = get_url.replace('https','http')
    #print(get_url)
    #get_url='https://www.21cnjy.com/H/2/90463/2308527.shtml'
    doma = ".21cnjy.com"
    response = requests.get(get_url, cookies=get_chrome_cookies(doma))
    soup = BeautifulSoup(response.text,'html.parser')#使用python默认的解析器
    
    testKGtag = soup.find('ul',class_="view-meta-list")
    try:
        global kgtest
        kgtest=''
        for kga in testKGtag.find_all('a'):
            kgtest=kgtest+" "+kga.get_text()
    except:
        ''
    downloadlink = soup.find('a',class_="nom-u btn")
    response = requests.get("https://www.21cnjy.com"+downloadlink['href'], cookies=get_chrome_cookies(doma))
    ss=response.text
    response = requests.get("https://www.21cnjy.com"+ss[ss.find("<a href")+11:ss.find('btn-download J_DownLoad')-11], cookies=get_chrome_cookies(doma))
    finalUrl = response.url
    response = urllib.request.urlopen(finalUrl).read()
    ff=open("G:/21edu/"+str(filename)+".zip",'wb')
    ff.write(response)
    ff.close()

def PageDownLoad(source,stage,subject,scopetext):
    global count
  
    soup = BeautifulSoup(source,'html.parser')#使用python默认的解析器
    linklist = soup.findAll('a',class_="btn-download")
    infolist = soup.findAll('div',class_='item-path')
    otherlist= soup.findAll('i','icon icon_course')
    
    for i in range(0,len(linklist)):
        link=linklist[i]
        info=infolist[i]
        ttyy=otherlist[i]
        cattext = ttyy.parent.get_text().strip()
        try:
            downloadDoc(link['href'],count)
            print(''.join(info.stripped_strings))
            try:
                global kgtest
                cur.execute("INSERT into resource(stage,subject,area,sidecat,cat,filename,kgtest)values('"+stage+"','"+subject+"','"+scopetext+"','"+''.join(info.stripped_strings)+"','"+cattext+"','"+str(count)+"','"+kgtest+"')")
                conn.commit()
            except Exception as e:
                print(e)
            print(count)
            count+=1
        except Exception as e:
            'print(e)' 
    
if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.21cnjy.com/9/23883/")
#     driver.get("http://passport.21cnjy.com/login?jump_url=http%3A%2F%2Fwww.21cnjy.com/")
#     driver.find_element_by_id('user-name').send_keys('18963567280')
#     driver.find_element_by_id('user-pwd').send_keys('chen1234')
#     bu = driver.find_element_by_xpath("//form[@class='my-form']/button")
#     ActionChains(driver).click(bu).perform()
    driver.set_page_load_timeout(20)
    
 
    havenext=True
    run=1
    while havenext and run>0:
        if run<2:
            con=input("continue?")
            if int(con)>1:
                run=2
        
        #print(driver.page_source)
        PageDownLoad(driver.page_source, "小学", "政治思品", "同步资源")
        #下一页
        
        try:
            bu = driver.find_element_by_class_name('next')
            ActionChains(driver).click(bu).perform()
            time.sleep(1)
        except:
            havenext=False
            
    driver.quit()
    
    
    