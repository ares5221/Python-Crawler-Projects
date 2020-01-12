# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    # allowed_domains = ['tencent.com']
    # start_urls = ['https://hr.tencent.com/position.php?&start=0']
    url = 'https://careers.tencent.com/search.html?&start='
    offset = 10
    start_urls = [url + str(offset)]

    def parse(self, response):
        # print(response.text)
        for each in response.xpath("//tr[@class = 'even'] | //tr[@class = 'odd']"):
            # 初始化模型对象
            item = TencentItem()

            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        # 方式一 拼接url
        # if self.offset < 100:
        #     self.offset += 10
        #     # 将请求重写发送给调度器入队列、出队列、交给下载器下载
        #     # 拼接新的url，并回调parse函数处理response
        #     # yield scrapy.Request(url， callback = self.parse)
        # yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

        # 方式二，读取下一页的按钮
        if len(response.xpath("//a[@class= 'noactive' and @id = 'next]")) ==0:
            url = response.xpath("//a[@id='next]/@href").extrace()[0]
            yield scrapy.Request('http://careers.tencent.com/'+url,callback=self.parse)








    http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20$offset=10