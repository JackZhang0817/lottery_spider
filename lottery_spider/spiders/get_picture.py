# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from lottery_spider.items import GetPicItem
from lottery_spider.settings import PIC_URL_SELF
from urllib import request

re_url = r'/(\d*).html'
re_img = r'src=(.*?)>'
re_ct_id = r'[/2017/|/](\d+).html'
re_year = r'(/d*).html'


class GetPictureSpider(scrapy.Spider):
    name = 'get_picture_list'
    allowed_domains = ['www.2mtk.cc']
    start_urls = ['http://www.2mtk.cc/2018.html']

    def parse(self, response):
        url = re.findall(re_url, response.url)
        se = Selector(response)
        list_li = se.xpath("//div[@class='a_list clearfix']/ul/li")
        print(len(list_li))
        for i in range(len(list_li)):
            pic_title_span = se.xpath("//div[@class='a_list clearfix']/ul/li[%d + 1]/span/text()" % i).extract()
            pic_title_a = se.xpath("//div[@class='a_list clearfix']/ul/li[%d + 1]/a/text()" % i).extract()
            if len(pic_title_a) < 1:
                pic_title_a = se.xpath("//div[@class='a_list clearfix']/ul/li[%d + 1]/a/strong/text()" % i).extract()
            pic_url = se.xpath("//div[@class='a_list clearfix']/ul/li[%d + 1]/a/@href" % i).extract()
            pic_qi_num = se.xpath("//div[@class='a_list clearfix']/ul/li[%d + 1]/label/a/text()" % i).extract()
            pic_ct_id = re.findall(re_ct_id, pic_url[0])
            pic_thumb = se.xpath("//div[@class='a_list clearfix']/ul/li[%d + 1]/a/@onmouseover" % i).extract()
            pic_thumb_img = re.findall(re_img, pic_thumb[0])
            item = GetPicItem()
            if not(len(pic_ct_id) > 0):
                continue
            # pass
            item['pic_ct_id'] = url[0] + pic_ct_id[0]
            item['pic_year'] = url[0]

            if len(pic_title_span) > 0:
                item['pic_title_span'] = pic_title_span[0]
            else:
                item['pic_title_span'] = ''

            if len(pic_title_a) > 0:
                item['pic_title'] = pic_title_a[0]
            else:
                item['pic_title'] = ''
            # item['pic_title'] = pic_title_span[0] + pic_title_a[0]
            if len(pic_thumb_img) > 0:
                # request.urlretrieve(pic_thumb_img[0], save_img_path)
                item['pic_thumb_url'] = pic_thumb_img[0]
            else:
                item['pic_thumb_url'] = ''

            item['pic_qi_num'] = pic_qi_num[0]
            yield item
