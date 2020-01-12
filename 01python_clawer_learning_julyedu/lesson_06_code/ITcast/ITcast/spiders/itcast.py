# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        print(response.body)
        # pass
