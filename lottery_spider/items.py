# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LotterySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    create_time = scrapy.Field()
    qi_num = scrapy.Field()
    ping_1 = scrapy.Field()
    ping_2 = scrapy.Field()
    ping_3 = scrapy.Field()
    ping_4 = scrapy.Field()
    ping_5 = scrapy.Field()
    ping_6 = scrapy.Field()
    ma_1 = scrapy.Field()
    ma_2 = scrapy.Field()
    ma_3 = scrapy.Field()
    ma_4 = scrapy.Field()
    ma_5 = scrapy.Field()
    ma_6 = scrapy.Field()
    special_ma = scrapy.Field()
    pass


class LotteryRecordItem(scrapy.Item):
    create_time = scrapy.Field()
    qi_num = scrapy.Field()
    ping_1 = scrapy.Field()
    ping_2 = scrapy.Field()
    ping_3 = scrapy.Field()
    ping_4 = scrapy.Field()
    ping_5 = scrapy.Field()
    ping_6 = scrapy.Field()
    ma_1 = scrapy.Field()
    ma_2 = scrapy.Field()
    ma_3 = scrapy.Field()
    ma_4 = scrapy.Field()
    ma_5 = scrapy.Field()
    ma_6 = scrapy.Field()
    special_ma = scrapy.Field()
