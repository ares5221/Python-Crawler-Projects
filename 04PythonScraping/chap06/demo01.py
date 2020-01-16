#!/usr/bin/env python
# _*_ coding:utf-8 _*_


title = "This is a test sentence."
with open('title.txt', "a+") as f:
    f.write(title)
    f.close()

title = "This is a test sentence."
with open(r'G:\pythonLearningWorkSpace\Python-Crawler-Projects\04PythonScraping\chap05\title.txt', "a+") as f:
    f.write(title)
    f.close()


title = "This is a test sentence."
with open('G:\\pythonLearningWorkSpace\\Python-Crawler-Projects\\04PythonScraping\chap05\\title.txt', "a+") as f:
    f.write(title)
    f.close()

with open('title.txt', "r", encoding ='utf-8') as f:
    result = f.read()
    print (result)