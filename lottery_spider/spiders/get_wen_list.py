# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import GetWenListItem


class GetWenListSpider(scrapy.Spider):
    name = 'get_wen_list'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['http://www.2m010.cc/']

    def parse(self, response):
        pass
