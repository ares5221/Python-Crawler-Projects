# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
# from settings import IMAGES_STORE as image_store

image_store = r'D:\python\Python-Crawler-Projects\03scrapy_demo\Douyu'
class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        image_like = item['imagelink']
        yield scrapy.Request(image_like)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok ]

        os.rename(image_store+image_path[0], image_store+item['nickname']+'.jpg')
        return item