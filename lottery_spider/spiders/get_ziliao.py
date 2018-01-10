# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GetZiliaoSpider(CrawlSpider):
    name = 'get_ziliao'
    allowed_domains = ['www.2m010.cc']
    download_delay = 1
    start_urls = ['http://www.2m010.cc/']

    rules = (
            Rule(LinkExtractor(allow=(r'/html/(\d*)_([1|2]).html'))),
            # Rule(LinkExtractor(allow=(r'/html/(\d*)_([1|2]).html'))),
            # Rule(LinkExtractor(allow=(r'/html/(\d*).html')),
            #      callback="parse_item",
            #      follow=True),
        )
    for i in rules:
        print(1111)
        print(i)

    def parse(self, response):
        pass
