# -*- coding: utf-8 -*-
import scrapy
from ITcastSpider.items import ItcastspiderItem

class ItcastspiderSpider(scrapy.Spider):
    name = 'itcastspider'
    allowed_domains = ['itcast.cn/']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # print(response.body)
        items = []
        # xpath可以根据chrome 插件xpath helper来验证
        for each in response.xpath('//div[@class = "li_txt"]'):
            item = ItcastspiderItem()
            # ./h3/text() 这个 . 表示从当前路径开始找
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            yield item
        #     这里方式1 采用列表items存储，推荐使用yield的方式直接返回item对象也就是这里用的方式2
        #     items.append(item)
        #     # 直接返回数据，用于保存类型
        # return items
