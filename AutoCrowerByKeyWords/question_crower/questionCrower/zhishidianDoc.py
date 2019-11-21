import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import pyHook
import time
import string
import os
import chardet
import checkLegal
import http.cookiejar
import urllib.parse
import urllib.error
import subprocess
import sqlite3
import win32crypt
import json
import pymysql
#id:学段，科目，区域，侧边目录，分类，zip文件名
# stage='小学'
# subject=''
# scopetext='知识点专区'
# sidetext=''
# cattext=''

conn = pymysql.connect("localhost", "root", "1234", "21edu",use_unicode=True, charset="utf8")
cur = conn.cursor()
count=18826
node=True
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

def mutPageDownLoad(baseurl,stage,subject,scopetext,sidetext,cattext):
    ok = True
    pagenum=1
    global count
    global node
    while ok:
        print("page:"+str(pagenum))
        url = baseurl+str(pagenum)
        print(url)
        if node :    
            if 'http://www.21cnjy.com/soft.php?mod=knowledgelist&chid=11&kid=3391&typeid=6&page=' in url:
                pagenum=1
                node=False
                print("hahaha")
                time.sleep(10)
            else:
                break
        doma = ".21cnjy.com"
        response = requests.get(url, cookies=get_chrome_cookies(doma))
#         if '暂无符合条件的记录' in response.text:
#             break
        if response.text.find("下一页")<0:
            try:
                sss = BeautifulSoup(response.text,'html.parser')
                
                ppp=sss.find('div',class_="site-pager xc").find_all('a')
                ff='mm'
                for ne in ppp:
                    ff=ne.get_text()
                if ff == str(pagenum) or ff=='mm':
                    ok=False    
            except:
                ok=False
            
        soup = BeautifulSoup(response.text,'html.parser')#使用python默认的解析器
        linklist = soup.findAll('a',class_="btn-download")
        infolist = soup.findAll('div',class_='item-path')
        for i in range(0,len(linklist)):
            
        #for link in linklist:
            link=linklist[i]
            info=infolist[i]
            
            try:
#                 if node:
#                     if '初中生物/人教版（新课程标准）/七年级上册/第一单元 生物和生物圈/第一章   认识生物/第一节  生物的特征' == ''.join(info.stripped_strings):
#                         node=False
#                     else
#                         continue
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
            except:
                ''    
        pagenum+=1
       
                
def gogo(baseurl): 
    doma = ".21cnjy.com"
    response = requests.get(baseurl, cookies=get_chrome_cookies(doma))
    soup = BeautifulSoup(response.text,'html.parser')
    
    subjectList = soup.findAll('div',class_="mc tabitem-bd")
    for subsubjectList in subjectList:
        linklist = subsubjectList.findAll('a')
        for link in linklist:
            stage='小学'
            subject=link.get_text()

            scopetext='知识点专区'
            url='http://www.21cnjy.com'+link['href']
            if 'xd=1' in link['href']:
                stage='小学'
            elif 'xd=2' in link['href']:
                stage='初中'
            elif 'xd=3' in link['href']:
                stage='高中'
            
            response1 = requests.get(url, cookies=get_chrome_cookies(doma))
            soup1 = BeautifulSoup(response1.text,'html.parser')    
            scope = soup1.find('ul',class_='nav-list fl')
            for scopelink in scope.findAll('a'):
                try:
                    scopetext=scopelink.get_text()
                    if '知识点专区' != scopetext:
                        continue
                    
                    surl='http://www.21cnjy.com'+scopelink['href']
                    sidetext="第一层"
                    #print(sidetext)
                    response3 = requests.get(surl, cookies=get_chrome_cookies(doma))
                    soup3 = BeautifulSoup(response3.text,'html.parser')    
                    caturls = soup3.find('div',class_='mc fold-mc')#"J_TypeFilter")
                    for cclink in caturls.findAll('a'):
                        try:
                            finalurl='http://www.21cnjy.com'+cclink['href']
                            cattext=cclink.get_text()
                            if '全部' != cattext:
                                mutPageDownLoad(finalurl+"&page=",stage,subject,scopetext,sidetext,cattext)
                        except:
                                    ''
                    
                    '''
                    scopeurl='http://www.21cnjy.com'+scopelink['href']
                    response2 = requests.get(scopeurl, cookies=get_chrome_cookies(doma))
                    soup2 = BeautifulSoup(response2.text,'html.parser')    
                    sideurls = soup2.find('div',class_="mt-inner")
                    for sideurl in sideurls.findAll('a'):
                        #侧边目录只有顶层
                        try:
                            surl='http://www.21cnjy.com'+sideurl['href']
                            sidetext=sideurl.get_text()
                            print(sidetext)
                            response3 = requests.get(surl, cookies=get_chrome_cookies(doma))
                            soup3 = BeautifulSoup(response3.text,'html.parser')    
                            caturls = soup3.find('ul',class_="J_TypeFilter")
                            for cclink in caturls.findAll('a'):
                                try:
                                    finalurl='http://www.21cnjy.com'+cclink['href']
                                    cattext=cclink.get_text()
                                    if '全部' != cattext:
                                        mutPageDownLoad(finalurl+"&page=")
                                except:
                                    ''
                        except:
                            ''
                    '''
                except:
                    ''
                
                   
        
                      
if __name__=='__main__':
    #baseurl=r'https://www.21cnjy.com/knowledge.php?chid=2&kid=4602&page='
#     baseurl=r'https://www.21cnjy.com/soft.php?mod=knowledgelist&chid=3&kid=61&typeid=4&page='
#     mutPageDownLoad(baseurl)
      
    getsubjecturl='http://www.21cnjy.com/knowledge.php?chid=2&kid=4602'
    gogo(getsubjecturl)
        
#<ul class="J_TypeFilter">
    
        #print(soup.prettify())

    
    