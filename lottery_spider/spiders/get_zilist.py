# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import GetCollectItem
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GetZilistSpider(CrawlSpider):
    name = 'get_zilist'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/html/328_1.html']
    rules = (
        Rule(LinkExtractor(allow=(r'https://www.2m010.cc/html/328_\d+.html')),
             callback="parse_item",
             follow=True),
    )
    for rule in rules:
        print(rule)


    def parse_item(self, response):
        print(response.url)
        se = Selector(response)
        se_tr = se.xpath("//div[@class='listbox']/ul/li")
        for i in range(len(se_tr) -1):
            title = se.xpath("//div[@class='listbox']/ul/li[%d + 1]/a/text()" % i).extract()
            if title != '':
                item = GetCollectItem()
                item['content'] =title[0]
                yield item


    '''
    def parse(self, response):
        se = Selector(response)
        se_tr = se.xpath("//div[@class='listbox']/ul/li").extract()[0]
        item = GetCollectItem()
        item['content'] = se_tr
        yield item
        pass
    '''
