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
    time = scrapy.Field()
    qi_num = scrapy.Field()
    ping_1 = scrapy.Field()
    ping_2 = scrapy.Field()
    ping_3 = scrapy.Field()
    ping_4 = scrapy.Field()
    ping_5 = scrapy.Field()
    ping_6 = scrapy.Field()
    se_1 = scrapy.Field()
    se_2 = scrapy.Field()
    se_3 = scrapy.Field()
    se_4 = scrapy.Field()
    se_5 = scrapy.Field()
    se_6 = scrapy.Field()
    ma_1 = scrapy.Field()
    ma_2 = scrapy.Field()
    ma_3 = scrapy.Field()
    ma_4 = scrapy.Field()
    ma_5 = scrapy.Field()
    ma_6 = scrapy.Field()
    special_ma = scrapy.Field()
    special_num = scrapy.Field()
    special_color = scrapy.Field()
    single = scrapy.Field()
    bo_color = scrapy.Field()
    min = scrapy.Field()
    five_elements = scrapy.Field()
    tetou = scrapy.Field()
    weishu = scrapy.Field()
    hedanshuang = scrapy.Field()
    jiaye = scrapy.Field()
    door_num = scrapy.Field()
    duan_num = scrapy.Field()
    yinyang = scrapy.Field()
    tiandi = scrapy.Field()
    jixiong = scrapy.Field()
    heibai = scrapy.Field()
    sexiao = scrapy.Field()
    bihua = scrapy.Field()
    sex = scrapy.Field()
    zonghe = scrapy.Field()


class TestTableItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()


class GetCollectItem(scrapy.Item):
    content = scrapy.Field()
    url = scrapy.Field()


class GetWenListItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    type_id = scrapy.Field()
    time = scrapy.Field()


class GetWenCtItem(scrapy.Item):
    ct_id = scrapy.Field()
    type_id = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    qi_num = scrapy.Field()
    img = scrapy.Field()
    content = scrapy.Field()
    abstract = scrapy.Field()
    create_time = scrapy.Field()
    create_by = scrapy.Field()
    update_time = scrapy.Field()


class GetPicItem(scrapy.Item):
    pic_title_span = scrapy.Field()
    pic_title = scrapy.Field()
    pic_qi_num = scrapy.Field()
    pic_year = scrapy.Field()
    pic_span = scrapy.Field()
    pic_url = scrapy.Field()
    pic_ct_id = scrapy.Field()
    pic_thumb_url = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()


class GetFreeDataItem(scrapy.Item):
    type_id = scrapy.Field()
    title = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()

