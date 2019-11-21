import urllib.request
import pymysql
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import string
import os

def getKnowledgeDict(url):
        knowledgeUrlDict=dict()
        response= urllib.request.urlopen(url).read()
        soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
        knowledgetree = soup.find('ul',class_='treeview',id="con_one_1")
        aa=knowledgetree.find_all('a')
        for hr in aa:
            knowledgeUrlDict[hr.get_text().strip()]=hr.get('href')
        
#         for (k,v) in  knowledgeUrlDict.items(): 
#             print (k,v) 
        return knowledgeUrlDict
    
def getSubjectDict(url):
    subjectDict = dict()
    response= urllib.request.urlopen(url).read()
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
    aa = root.find_all('p')
    for hr in aa:
        if '题型' in hr.get_text():
            for hr in hr.find_all('a'):
                if '全部' != hr.get_text().strip():
                    typeDict[hr.get_text().strip()]=hr.get('href')
    return typeDict


def getKnowledge(url,stage,subject,knowledge,type,conn,cur):
    #化学基本概念与原理 单选 化学 初中
    response= urllib.request.urlopen(url).read()
    soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
    last = soup.find('a',class_='last')
    pagenum=1
    try:
        pagenum = int(last.get_text().strip()[3:].strip())+1
        if int(last.get_text().strip()[3:].strip())>100:
            pagenum=101
    except:
        ''
    
    for page in range(1,pagenum):
        response= urllib.request.urlopen(url+'&page='+str(page)).read()
        soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
        questions = soup.find('div',class_='questions_col')
        for tag in questions.children:
            if tag.name=='ul':
                for subtag in tag.children:
                    if subtag.name=='li':
                        question=''
                        choice=''
                        analysis=''
                        answer=''
                        imagesrc=''
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
    ok=False
    stageDict={'初中':'2','高中':'3'}
    for (k,v) in  stageDict.items(): 
        stage=k
        subjectDict = getSubjectDict('http://tiku.21cnjy.com/tiku.php?mod=quest&channel=2&xd='+v)
        for (sk,sv) in subjectDict.items():
            subject=sk 
            knowledgeDict = getKnowledgeDict('http://tiku.21cnjy.com/'+sv)
            for (nk,nv) in knowledgeDict.items(): 
                knowledge=nk
                if knowledge == '主语从句' and stage=='高中':
                    ok=True
                if ok :
                    #print(nv)
                    typeDict = getTypeDict('http://tiku.21cnjy.com/tiku.php'+nv)
                    for (tk,tv) in typeDict.items(): 
                        type=tk
                        try:
                            getKnowledge('http://tiku.21cnjy.com/'+tv,stage,subject,knowledge,type,conn,cur)
                        except:
                            ''

if __name__=='__main__':
    main()