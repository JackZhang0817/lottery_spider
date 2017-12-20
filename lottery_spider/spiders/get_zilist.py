# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import GetCollectItem
from scrapy.selector import Selector


class GetZilistSpider(scrapy.Spider):
    name = 'get_zilist'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/html/328_1.html']

    def parse(self, response):
        se = Selector(response)
        se_tr = se.xpath("//div[@class='listbox']/ul/li").extract()[0]
        item = GetCollectItem()
        item['content'] = se_tr
        yield item
        pass
