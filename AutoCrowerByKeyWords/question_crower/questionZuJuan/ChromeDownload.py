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
from _pytest import tmpdir


conn = pymysql.connect("172.22.113.22", "aicfe", "aicfe", "question",use_unicode=True, charset="utf8")
cur = conn.cursor()



def DownLoad(driver,stage,subject):
    havenext=True
    while havenext:   
        roothandle = driver.current_window_handle
        jiexilist = driver.find_elements_by_class_name('icona-jiexi')
        
        for jiexi in jiexilist:
            try:
                time.sleep(3)
                ActionChains(driver).click(jiexi).perform()
                time.sleep(3)
               
                for hand in driver.window_handles:
                    if hand == roothandle:
                        continue
                    driver.switch_to_window(hand)
                    time.sleep(3)
                    
                    type = driver.find_element_by_xpath("//p[@class='exam-head-left']/span[1]").get_attribute('textContent').split('：')[1].strip()
                    cat = driver.find_element_by_xpath("//p[@class='exam-head-left']/span[2]").get_attribute('textContent').split('：')[1].strip()
                    degree = driver.find_element_by_xpath("//p[@class='exam-head-left']/span[3]").get_attribute('textContent').split('：')[1].strip()
                    source=''
                    try:
                        source = driver.find_element_by_xpath("//p[@class='exam-head-right']/span").get_attribute('textContent').strip()
                    except:
                        ''
                    
                    soup = BeautifulSoup(driver.page_source,'html.parser')
                    question = ''
                    qq = soup.find('div',class_='exam-con')
                    for que in qq.findAll('div',class_='exam-q'):
                        question = question+''.join(que.stripped_strings)+"\n"
           
    
                    for con in qq.find_all('div',class_='exam-con'):
                        question = question+''.join(con.stripped_strings)+'\n'
    
                    question=question.strip()
                    choice=''
                    try:
                        choice = '\n'.join(qq.find('div',class_='exam-s').stripped_strings)
                    except:
                        ''
                    
                    knowledge=''
                    answer=''
                    analysis=''
                    
                    if qq.find('div',class_='exam-qlist'):
                        try:
                            for an in qq.findAll('div',class_='analyticbox-body'):
                                answer = answer + ''.join(an.stripped_strings)+"\n"    
                            brick=soup.find('div',class_='analyticbox-brick')
                            knowledge = brick.find('div',class_='analyticbox').find('div',class_='analyticbox-body').get_text()
                            analysis=brick.find('div',class_='analyticbox analyticbox1').find('div',class_='analyticbox-body').get_text()
                        except:
                            ''
                    else:
                        try:  
                            bb=soup.find('div',class_='analyticbox-brick analyticbox-brick-normal')   
                            for kaoan in bb.findAll('div',class_='analyticbox'):
                                tmp = ''.join(kaoan.stripped_strings)
                                if '【考点】' in tmp:
                                    knowledge=tmp
                                elif '【答案】' in tmp:
                                    answer=tmp
                            analysis=''.join(bb.find('div',class_='analyticbox analyticbox1').stripped_strings)
                        except:
                            ''
                    
                    global conn
                    global cur
                    try:
                        
                        cur.execute("INSERT into zujuanquestion(stage,subject,type,cat,degree,source,question,choice,answer,knowledge,analysis)values('"+stage+"','"+subject+"','"+type+"','"+cat+"','"+degree+"','"+source+"','"+question+"','"+choice+"','"+answer+"','"+knowledge+"','"+analysis+"')")
                        conn.commit()
                    except:
                        ''
                    #登录
    #                 login = driver.find_element_by_class_name('loginbox')
    #                 ActionChains(driver).click(login).perform()
    #                  
    #                 driver.find_element_by_id('account').send_keys('18963567280')
    #                 driver.find_element_by_id('password').send_keys('chen1234')
    #                 but = driver.find_element_by_class_name('reg-btn')
    #                 ActionChains(driver).click(but).perform()
    #                 time.sleep(3)
                    
    #                 logout = driver.find_element_by_xpath('//div[@class="drop-bd"]/ul/li[8]')
    #                 ActionChains(driver).click(logout).perform()
    #                 Actions actions = new Actions(driver);
    #                 actions.moveToElement(WebElement).perform();
                    
                    driver.close()
                driver.switch_to_window(roothandle)
            except:
                driver.switch_to_window(roothandle) 
        #下一页       
        try:
            bu = driver.find_element_by_link_text('下一页')
            ActionChains(driver).click(bu).perform()
            time.sleep(3)
        except:
            havenext=False
            
    driver.quit()


        
if __name__=='__main__':

# driver = webdriver.Chrome()
#                 driver.maximize_window()
#                 #driver.get("http://zujuan.21cnjy.com/question?chid=2&xd=1&tree_type=knowledge")
#                 driver.get("http://passport.21cnjy.com/login?jump_url=http%3A%2F%2Fwww.21cnjy.com/")
#                 driver.find_element_by_id('user-name').send_keys('18963567280')
#                 driver.find_element_by_id('user-pwd').send_keys('chen1234')
#                 bu = driver.find_element_by_xpath("//form[@class='my-form']/button")
#                 ActionChains(driver).click(bu).perform()
#                 driver.set_page_load_timeout(20)
    
    subjectdict=dict() 
    subjectdict[2]='语文'
    subjectdict[3]='数学'
    subjectdict[4]='英语'
    subjectdict[5]='科学'
    subjectdict[6]='物理'
    subjectdict[7]='化学'
    subjectdict[8]='历史'
    subjectdict[9]='政治思品'
    subjectdict[10]='地理'
    subjectdict[11]='生物'
    subjectdict[20]='历史与社会'
    subjectdict[21]='社会思品'

    stage=''
    for i in range(1,4):
        if i == 1:
            stage="小学"
            for j in [2,3,4,5,9]:

                driver = webdriver.Chrome()
                driver.maximize_window()
                #driver.get("http://zujuan.21cnjy.com/question?chid=2&xd=1&tree_type=knowledge")
                driver.set_page_load_timeout(20)
                url='http://zujuan.21cnjy.com/question?chid='+str(j)+'&xd='+str(i)+'&tree_type=knowledge'
                driver.get(url)
                login = driver.find_element_by_class_name('loginbox')
                ActionChains(driver).click(login).perform()
                  
                driver.find_element_by_id('account').send_keys('18963567280')
                driver.find_element_by_id('password').send_keys('chen1234')
                but = driver.find_element_by_class_name('reg-btn')
                ActionChains(driver).click(but).perform()
                logout = driver.find_element_by_xpath('//div[@class="drop-bd"]/ul/li[8]')
                
                ActionChains(driver).click(logout).perform()
                time.sleep(3)
                DownLoad(driver, stage, subjectdict[j])
                
                
        elif i == 2:
            stage="初中"
            for j in [2,3,4,5,6,7,8,9,10,11,20,21]:
                driver = webdriver.Chrome()
                driver.maximize_window()
                driver.set_page_load_timeout(20)
                url='http://zujuan.21cnjy.com/question?chid='+str(j)+'&xd='+str(i)+'&tree_type=knowledge'
                driver.get(url)
                login = driver.find_element_by_class_name('loginbox')
                ActionChains(driver).click(login).perform()
                  
                driver.find_element_by_id('account').send_keys('18963567280')
                driver.find_element_by_id('password').send_keys('chen1234')
                but = driver.find_element_by_class_name('reg-btn')
                ActionChains(driver).click(but).perform()
                logout = driver.find_element_by_xpath('//div[@class="drop-bd"]/ul/li[8]')
                ActionChains(driver).click(logout).perform()
                time.sleep(3)
                DownLoad(url, driver, stage, subjectdict[j])
                
        else:
            stage="高中"
            for j in [2,3,4,6,7,8,9]:
                driver = webdriver.Chrome()
                driver.maximize_window()
                driver.set_page_load_timeout(20)
                url='http://zujuan.21cnjy.com/question?chid='+str(j)+'&xd='+str(i)+'&tree_type=knowledge'
                driver.get(url)
                login = driver.find_element_by_class_name('loginbox')
                ActionChains(driver).click(login).perform()
                  
                driver.find_element_by_id('account').send_keys('18963567280')
                driver.find_element_by_id('password').send_keys('chen1234')
                but = driver.find_element_by_class_name('reg-btn')
                ActionChains(driver).click(but).perform()
                logout = driver.find_element_by_xpath('//div[@class="drop-bd"]/ul/li[8]')
                ActionChains(driver).click(logout).perform()
                time.sleep(3)
                DownLoad(url, driver, stage, subjectdict[j])
                
                
   
    
    
    
    
    