# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import LotteryRecordItem


class LotteryRecordSpider(scrapy.Spider):
    name = 'lottery_record'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/history/2017.html']

    def parse(self, response):
        record_html = response.xpath("//div[re:test(@id, 'main')]").extract()
        record2_html = response.css('#main').extract()
        record_item = LotteryRecordItem()
        record_item['create_time'] = record2_html
        yield record_item


