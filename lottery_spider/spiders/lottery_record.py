# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import LotteryRecordItem
from lottery_spider.items import TestTableItem


class LotteryRecordSpider(scrapy.Spider):
    name = 'lottery_record'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/history/2017.html']

    def parse(self, response):
        record_html = response.xpath("//div[re:test(@id, 'main')]")
        item = TestTableItem()
        item['name'] = record_html.xpath('//td[1]').extract()
        item['url'] = record_html.xpath('//td[2]').extract()
        yield item
        # for sel in record_html.xpath('//tr'):
        #     item = TestTableItem()
        #     item['name'] = sel.xpath('//td[1]').extract()
        #     item['url'] = sel.xpath('//td[2]').extract()
        #     yield item
        # record2_html = response.css('#main').extract()
        # record_item = LotteryRecordItem()
        # record_item['create_time'] = record2_html
        # yield record_item


