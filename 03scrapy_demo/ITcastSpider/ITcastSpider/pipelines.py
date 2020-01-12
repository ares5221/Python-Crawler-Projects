# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ItcastspiderPipeline(object):

    # __init__可选的，初始化文件
    def __init__(self):
        self.filename = open("itcast_info.json", "wb")

    # 处理Item数据的，必须写的
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))
        return item

    # 可选的，执行结束时的方法
    def close_spider(self, spider):
        self.filename.close()

