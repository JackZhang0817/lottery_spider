# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import GetWenListItem
from scrapy.selector import Selector
import re


class GetWenListSpider(scrapy.Spider):
    name = 'get_wen_list'
    allowed_domains = ['www.2m010.cc']
    # start_urls = ['http://www.2m010.cc/html/ziliao.html']
    start_urls = ['http://www.2m010.cc/html/253672.html']


    def parse(self, response):
        se = Selector(response)

        se_tr = se.xpath("//div[@class='mcc_content']/ul/li")
        for i in range(len(se_tr)):
            title = se.xpath("//div[@class='mcc_content']/ul/li[%d + 1]/a/text()" % i).extract()
            url = se.xpath("//div[@class='mcc_content']/ul/li[%d + 1]/a/@href" % i).extract()
            item = GetWenListItem()
            item['title'] = title[0]
            item['url'] = url[0]
            re_t = r'(\d*)_1.html'
            m = re.findall(re_t, url[0])
            item['type_id'] = m[0]
            yield item



