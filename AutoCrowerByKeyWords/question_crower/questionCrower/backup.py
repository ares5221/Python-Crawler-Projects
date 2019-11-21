import urllib.request
import pymysql
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import string
import os

def getKnowledgeDict():
        knowledgeUrlDict=dict()
        response= urllib.request.urlopen('http://tiku.21cnjy.com/tiku.php?mod=list&channel=7&xd=2').read()
        soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
        knowledgetree = soup.find('ul',class_='treeview',id="con_one_1")
        aa=knowledgetree.find_all('a')
        for hr in aa:
            knowledgeUrlDict[hr.get_text().strip()]=hr.get('href')
        
        for (k,v) in  knowledgeUrlDict.items(): 
            print (k,v) 
        return knowledgeUrlDict
    
def getSubjectDict(url):
    subjectDict = dict()
    response= urllib.request.urlopen(rul).read()
    soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
    root = soup.find('div',class_='catagory frame shiti_top')
    aa=root.find_all('p')
    for hr in aa:
        if '学科' in hr.get_text():
            for hr in hr.find_all('a'):
                subjectDict[hr.get_text().strip()]=hr.get('href')
    return subjectDict

def getTypeDict(url):
    typeDict = dict()
    response= urllib.request.urlopen(url).read()
    soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
    root = soup.find('div',class_='catagory frame shiti_top')
    aa=root.find_all('p')
    for hr in aa:
        if '题型' in hr.get_text():
            for hr in hr.find_all('a'):
                typeDict[hr.get_text().strip()]=hr.get('href')
    return typeDict

def getKnowledge():
    #化学基本概念与原理 单选 化学 初中
    response= urllib.request.urlopen('http://tiku.21cnjy.com/tiku.php?mod=quest&channel=7&xd=2&cid=302&type=1&page=2').read()
    soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
    last = soup.find('a',class_='last')
    pagenum=1
    try:
        pagenum = int(last.get_text().strip()[3:].strip())+1
        if int(last.get_text().strip()[3:].strip())>100:
            pagenum=101
    except:
        print(last.get_text())
    
    for page in range(1,pagenum):
        response= urllib.request.urlopen('http://tiku.21cnjy.com/tiku.php?mod=quest&channel=7&xd=2&cid=302&type=1&page='+str(page)).read()
        soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
        questions = soup.find('div',class_='questions_col')
        for tag in questions.children:
            if tag.name=='ul':
                for subtag in tag.children:
                    if subtag.name=='li':
                        question=''
                        choice=''
                        type='单选题'
                        subject='化学'
                        knowledge='身边的化学物质,空气和水,制取氧气'
                        stage='初中'
                        analysis=''
                        answer=''
                        imagesrc=''
                        #question
                        #print(subtag.stripped_strings)
    #                     for ss in subtag.contents:                       
    #                         if '<br' in str(ss):
    #                             f.write('\n')
    #                             print('\n')
    #                             break;
    #                         print(ss)
    #                         f.write(str(ss).strip())
    #                     for ss in subtag.stripped_strings:
    #                         f.write(ss+'\n')
    #                         print(ss)
    #                         break
                        #choise
                        result=''
                        for sstag in subtag.children:
                            if sstag.name=='img':
                                imagesrc=imagesrc+sstag.get('src')+' '
                            if sstag.name=='table':    
                                for ssstag in sstag.descendants:
                                    if ssstag.name=='td':
                                        for subss in ssstag.stripped_strings:
                                            result=result+subss+'\n'
                                            break
                            if sstag.name=='p':
                                #print(sstag)
                                for ans in sstag.children:
                                    try:
                                        if ans.get_text().strip()=='查看解析':
                                            ansresponse= urllib.request.urlopen('http://tiku.21cnjy.com/'+ans.get('href').strip()).read()
                                            anssoup = BeautifulSoup(ansresponse,'html.parser')#使用python默认的解析器
                                            anstag = anssoup.find('span',class_='option')
                                            answer=anstag.nextSibling.get_text()
                                            
                                            analysistag = anssoup.find('span',class_='parsing')
                                            analysis=analysistag.nextSibling.get_text()
                                            break
                                    except:
                                        ''
                                    #print(ans)
#                                     if ans.class_=="view_all":
#                                         print(ans['href'])
                            try:
                                sstag.clear()
                            except:
                                ''
                        tmp=''
                        for ss in subtag.stripped_strings:
                              tmp=tmp+ss
                        question=tmp
                        choice=result
                        try:
                            cur.execute("INSERT into question(question,choice,type,subject,knowledge,stage,analysis,answer,imagesrc)values('"+question+"','"+choice+"','"+type+"','"+subject+"','"+knowledge+"','"+stage+"','"+analysis+"','"+answer+"','"+imagesrc+"')")
                            conn.commit()
                        except:
                            'sql error'

def main():
    conn = pymysql.connect("172.22.113.22", "aicfe", "aicfe", "question",use_unicode=True, charset="utf8")
    cur = conn.cursor()
#     f=open('re.txt','w',encoding='utf-8')
#     
#     cur.execute("INSERT into question(question,choice,type,subject,knowledge,stage,analysis,answer,imagesrc)values('"+question+"','"+choice+"','"+type+"','"+subject+"','"+knowledge+"','"+stage+"','"+analysis+"','"+answer+"','"+imagesrc+"')")
#     conn.commit()


#     for page in range(1,101):
#         
#         response= urllib.request.urlopen('http://tiku.21cnjy.com/tiku.php?mod=quest&channel=7&xd=2&page='+str(page)).read()
#         soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
#         #f.write(soup.prettify())
#         questions = soup.find('div',class_='questions_col')
#         
#         deltags = soup.find_all(class_='hidejammersa')
#         for dd in deltags:
#             #print(dd)
#             dd.clear()
#         
#         deltags = soup.find_all(class_='this_jammer')
#         for dd in deltags:
#             #print(dd)
#             dd.clear()    
#         deltags = soup.find_all(class_='jammerd42')
#         for dd in deltags:
#             #print(dd)
#             dd.clear()    
#             
#             
#         for tag in questions.children:
#             if tag.name=='ul':
#                 for subtag in tag.children:
#                     if subtag.name=='li':
#                         #question
#                         for ss in subtag.stripped_strings:
#                             if ss != '查看解析' and ss != '添加到组卷':
#                                 print(ss)
#                                 f.write(ss+'\n')
#                         f.write('\n-----------------\n')
#     f.close()

    #化学基本概念与原理 单选 化学 初中
    response= urllib.request.urlopen('http://tiku.21cnjy.com/tiku.php?mod=quest&channel=7&xd=2&cid=302&type=1&page=2').read()
    soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
    last = soup.find('a',class_='last')
    pagenum=1
    try:
        pagenum = int(last.get_text().strip()[3:].strip())+1
        if int(last.get_text().strip()[3:].strip())>100:
            pagenum=101
    except:
        print(last.get_text())
    
    for page in range(1,pagenum):
        response= urllib.request.urlopen('http://tiku.21cnjy.com/tiku.php?mod=quest&channel=7&xd=2&cid=302&type=1&page='+str(page)).read()
        soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
        questions = soup.find('div',class_='questions_col')
        for tag in questions.children:
            if tag.name=='ul':
                for subtag in tag.children:
                    if subtag.name=='li':
                        question=''
                        choice=''
                        type='单选题'
                        subject='化学'
                        knowledge='身边的化学物质,空气和水,制取氧气'
                        stage='初中'
                        analysis=''
                        answer=''
                        imagesrc=''
                        #question
                        #print(subtag.stripped_strings)
    #                     for ss in subtag.contents:                       
    #                         if '<br' in str(ss):
    #                             f.write('\n')
    #                             print('\n')
    #                             break;
    #                         print(ss)
    #                         f.write(str(ss).strip())
    #                     for ss in subtag.stripped_strings:
    #                         f.write(ss+'\n')
    #                         print(ss)
    #                         break
                        #choise
                        result=''
                        for sstag in subtag.children:
                            if sstag.name=='img':
                                imagesrc=imagesrc+sstag.get('src')+' '
                            if sstag.name=='table':    
                                for ssstag in sstag.descendants:
                                    if ssstag.name=='td':
                                        for subss in ssstag.stripped_strings:
                                            result=result+subss+'\n'
                                            break
                            if sstag.name=='p':
                                #print(sstag)
                                for ans in sstag.children:
                                    try:
                                        if ans.get_text().strip()=='查看解析':
                                            ansresponse= urllib.request.urlopen('http://tiku.21cnjy.com/'+ans.get('href').strip()).read()
                                            anssoup = BeautifulSoup(ansresponse,'html.parser')#使用python默认的解析器
                                            anstag = anssoup.find('span',class_='option')
                                            answer=anstag.nextSibling.get_text()
                                            
                                            analysistag = anssoup.find('span',class_='parsing')
                                            analysis=analysistag.nextSibling.get_text()
                                            break
                                    except:
                                        ''
                                    #print(ans)
#                                     if ans.class_=="view_all":
#                                         print(ans['href'])
                            try:
                                sstag.clear()
                            except:
                                ''
                        tmp=''
                        for ss in subtag.stripped_strings:
                              tmp=tmp+ss
                        question=tmp
                        choice=result
                        try:
                            cur.execute("INSERT into question(question,choice,type,subject,knowledge,stage,analysis,answer,imagesrc)values('"+question+"','"+choice+"','"+type+"','"+subject+"','"+knowledge+"','"+stage+"','"+analysis+"','"+answer+"','"+imagesrc+"')")
                            conn.commit()
                        except:
                            'sql error'
                        #break
    #                     for ss in subtag.stripped_strings:
    #                         print(ss)
    #                         if ss!='查看解析' and ss!='添加到组卷':
    #                             f.write(ss)
    #                         
    #                     f.write('-------------\n')
    #         if len(str(tag).strip())>0:
    #             for sub in tag.descendants:
    #                 print(sub)
    #                 #print(str(sub).strip())
    #                 print('--\n')
    
        #print(questions.get_text().strip())
      
        #    time.sleep(5)
        #for each in soup.find_all(href = re.compile('view')):
        #    print(each.text,'->',''.join(['http://baike.baidu.com/',each['href']]))#join函数明显比+提高
 

if __name__=='__main__':
    main()