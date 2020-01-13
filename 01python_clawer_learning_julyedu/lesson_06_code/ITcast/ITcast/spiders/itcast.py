# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem

class ItcaseSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许爬虫作用的范围
    allowed_domains = ['http://www.itcast.cn/']
    # 爬虫开始的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#ajavaee"]



    # setting -> name -> allowed_domains ->start_urls -> request
    # request -> scrapy engine -> scheduler -> downloader -> download from inetrnet（自动执行）
    # Downloader -> spider ->调用parse方法
    def parse(self, response):
        # with open("teacher.html", 'wb') as f:
        #     f.write(response.body)  # 读取响应文件内容

        # 所有老师列表集合
        teacherItem = []

        for each in response.xpath('//div[@class = "li_txt"]'):
            # 将我们得到的数据封装到一个 `MyspiderItem` 对象
            item = ItcastItem()

            # 通过extract()转换为unicode字符串
            # 不加extract()就是xpath匹配的对象而已
            name = each.xpath('./h3/text()').extract()  # xpath返回的都是列表，元素根据匹配规则来(e.g. text())
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            item['name'] = name [0]
            item['title'] = title[0]
            item['info'] = info[0]

            teacherItem.append(item)
            # 直接返回数据，用于保存类型
        return teacherItem
