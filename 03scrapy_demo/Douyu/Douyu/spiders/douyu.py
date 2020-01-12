# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    # allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [base_url +str(offset)]
    print(start_urls)
    def parse(self, response):
        # print(response.body)
        data_list = json.loads(response.body_as_unicode())['data']
        if not len(data_list):
            return
        try:
            for data in data_list:
                item = DouyuItem()

                item['nickname'] = data['nickname']
                item['imagelink'] = data['vertical_src']
                yield  item

            self.offset +=20
            yield scrapy.Request(self.base_url+str(self.offset), callback=self.parse)
        except Exception as e:
            print (e)