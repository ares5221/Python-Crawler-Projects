#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
import json
def getjson(loc):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    pa = {
        'q': '公园',
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': 0,
        'output': 'json',
        'ak': 'DDtVK6HPruSSkqHRj5gTk0rc'
    }
    r = requests.get("http://api.map.baidu.com/place/v2/search", params=pa, headers= headers)
    decodejson = json.loads(r.text)
    return decodejson

province_list = ['江苏省', '浙江省', '广东省', '福建省', '山东省', '河南省', '河北省', '四川省', '辽宁省', '云南省',
                 '湖南省', '湖北省', '江西省', '安徽省', '山西省', '广西壮族自治区', '陕西省', '黑龙江省', '内蒙古自治区',
                 '贵州省', '吉林省', '甘肃省', '新疆维吾尔自治区', '海南省', '宁夏回族自治区', '青海省', '西藏自治区']
with open('cities1.txt', "a+", encoding='utf-8') as f:
    for eachprovince in province_list:
        decodejson = getjson(eachprovince)
        print(decodejson)
        for eachcity in decodejson['results']:
            city = eachcity['name']
            num = eachcity['num']
            output = '\t'.join([city, str(num)]) + '\r\n'

            f.write(output)
            # f.close()