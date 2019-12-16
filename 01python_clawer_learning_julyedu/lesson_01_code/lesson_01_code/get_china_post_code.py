import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate
import time

'''
本程序用来爬取IP138网站的数据，获取每个省份的市区邮编及区号信息
'''


class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    # 处理标签开始
    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    # 处理标签结束
    def end_element(self, name):
        pass

    # 文本处理
    def char_data(self, text):
        pass


def get_province_entry(url):
    # 获取文本，并用gb2312解码
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}

    requests.adapters.DEFAULT_RETRIES = 5
    content = requests.get(url, headers=headers).content.decode('gb2312')

    # 确定要查找字符串的开始结束位置，并用切片获取内容。
    start = content.find('<map name=\"map_86\" id=\"map_86\">')
    end = content.find('</map>')
    print(start, end)
    content = content[start:end + len('</map>')].strip()
    provinces = []
    # 生成Sax处理器
    handler = DefaultSaxHandler(provinces)
    # 初始化分析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    # 解析数据
    parser.Parse(content)
    # 结果字典为每一页的入口代码
    return provinces


if __name__ == '__main__':
    provinces = get_province_entry('http://www.ip138.com/post')
    print(provinces)
    # todo 对于爬取的信息，拼接对应号码后获取每个省的市区邮编信息，保存
