import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import string
import os
from sympy.interactive.tests.test_ipython import readline

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


    #get knowledge tree  (name,url)
    
    # 学科
   
        
       
        
        
#     for tag in knowledgetree.descendants:
#         try:    
#             name=tag.get_text().strip()
#             if len(name)>0:
#                 print(name)
#         
#         except:
#             ''
            
#     for tag in questions.children:
#         if tag.name=='ul':
#             for subtag in tag.children:
#                 if subtag.name=='li':
#                     #question
#                     #print(subtag.stripped_strings)
# #                     for ss in subtag.contents:                       
# #                         if '<br' in str(ss):
# #                             f.write('\n')
# #                             print('\n')
# #                             break;
# #                         print(ss)
# #                         f.write(str(ss).strip())
# #                     for ss in subtag.stripped_strings:
# #                         f.write(ss+'\n')
# #                         print(ss)
# #                         break
#                     #choise
#                     result=''
#                     for sstag in subtag.children:
#                         if sstag.name=='img':
#                             result=result+sstag.get('src')+'\n'
#                         if sstag.name=='table':    
#                             for ssstag in sstag.descendants:
#                                 if ssstag.name=='td':
#                                     for subss in ssstag.stripped_strings:
#                                         result=result+subss+'\n'
#                                         break
#                         try:
#                             sstag.clear()
#                         except:
#                             ''
#                     tmp=''
#                     for ss in subtag.stripped_strings:
#                           tmp=tmp+ss
#                     result=tmp+"\n"+result
#                     f.write(result)
#                     f.write('---------\n')
# 
#     f.close()
 

if __name__=='__main__':
    files = os.listdir('E:/baicizhan/IELTS/image')
    for fi in files:
        print(str(fi),str(fi)[0:str(fi).find('.')])
        break
#         if str(fi).endswith('docx'):
    
    
#     run=1
#     while run>0:
#         if run<2:
#             con=input("continue?")
#             if int(con)>1:
#                 run=2
#     
#         print("always run")