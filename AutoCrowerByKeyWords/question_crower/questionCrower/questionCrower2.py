import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import string
import os
def main():
    f=open('re.txt','w',encoding='utf-8')
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


    response= urllib.request.urlopen('http://tiku.21cnjy.com/tiku.php?mod=quest&channel=7&xd=2&page=3').read()
    soup = BeautifulSoup(response,'html.parser')#使用python默认的解析器
    questions = soup.find('ul',class_='treeview',id='con_one_1')
    for tag in questions.children:
        if tag.name=='ul':
            for subtag in tag.children:
                if subtag.name=='li':
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
                            result=result+sstag.get('src')+'\n'
                        if sstag.name=='table':    
                            for ssstag in sstag.descendants:
                                if ssstag.name=='td':
                                    for subss in ssstag.stripped_strings:
                                        result=result+subss+'\n'
                                        break
                        try:
                            sstag.clear()
                        except:
                            ''
                    tmp=''
                    for ss in subtag.stripped_strings:
                          tmp=tmp+ss
                    result=tmp+"\n"+result
                    f.write(result)
                    f.write('---------\n')
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
    f.close()
 

if __name__=='__main__':
    main()