# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import LotteryRecordItem
from scrapy.selector import Selector


class LotteryRecordSpider(scrapy.Spider):
    name = 'lottery_record'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/history/2017.html']

    def parse(self, response):
        se = Selector(response)
        se_tr = se.xpath("//div[@id='main']//tr")

        # se_td = se.xpath("//div[@id='main']//tr[2]/td[2]/a/text()").extract()
        for i in range(len(se_tr) - 1):
            create_time = se.xpath("//div[@id='main']//tr[%d + 2]/td[2]/a/text()" % i).extract()
            qi_num = se.xpath("//div[@id='main']//tr[%d + 2]/td[3]/a/text()" % i).extract()
            ping_1 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[1]/div[2]/text()" % i).extract()
            ping_2 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[2]/div[2]/text()" % i).extract()
            ping_3 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[3]/div[2]/text()" % i).extract()
            ping_4 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[4]/div[2]/text()" % i).extract()
            ping_5 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[5]/div[2]/text()" % i).extract()
            ping_6 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[6]/div[2]/text()" % i).extract()
            ma_1 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[1]/div[1]/text()" % i).extract()
            ma_2 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[2]/div[1]/text()" % i).extract()
            ma_3 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[3]/div[1]/text()" % i).extract()
            ma_4 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[4]/div[1]/text()" % i).extract()
            ma_5 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[5]/div[1]/text()" % i).extract()
            ma_6 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[6]/div[1]/text()" % i).extract()
            special_num = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[6]/div[1]/text()" % i).extract()

            item = LotteryRecordItem()
            item['create_time'] = create_time[0]
            item['qi_num'] = qi_num
            item['ping_1'] = ping_1
            item['ping_2'] = ping_2
            item['ping_3'] = ping_3
            item['ping_4'] = ping_4
            item['ping_5'] = ping_5
            item['ping_6'] = ping_6
            item['ma_1'] = ma_1
            item['ma_2'] = ma_2
            item['ma_3'] = ma_3
            item['ma_4'] = ma_4
            item['ma_5'] = ma_5
            item['ma_6'] = ma_6
            yield item
        # for i in range(len(se_tr)):
        #     create_time = se.xpath("//div[@id='main']/tr[%d]/td[2]/a/@text" % i).extract()
        #     qi_num = se.xpath("//div[@id='main']/tr[%d]/td[3]/a/@text" % i).extract()
        #     item = LotteryRecordItem()
        #     item['create_time'] = create_time
        #     item['qi_num'] = qi_num
        #     yield item
        # for sel in record_html.xpath('//tr'):
        #     item = TestTableItem()
        #     item['name'] = sel.xpath('//td[1]').extract()
        #     item['url'] = sel.xpath('//td[2]').extract()
        #     yield item
        # record2_html = response.css('#main').extract()
        # record_item = LotteryRecordItem()
        # record_item['create_time'] = record2_html
        # yield record_item


