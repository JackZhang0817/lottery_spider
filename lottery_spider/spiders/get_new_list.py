# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from lottery_spider.items import GetWenCtItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib import request
from lottery_spider.settings import PIC_URL_SELF
from database import MySQL
import re

re_qiid = r'(\d*)期'
re_ctid = r'/html/(\d*).html'
re_ctid2 = r'aid=(\d*)'
re_typeid = r'(\d*)_\d*.html'
re_time = r'.*?：(.*?$)'
datebase = MySQL()


class GetNewListSpider(scrapy.Spider):
    name = 'get_new_list'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/html/4_1.html']
    # result = datebase.query_dic({
    #     'delete': 'lt_new_list',
#     'where': {'type_id': 4}
    # })

    def parse(self, response):
        se = Selector(response)
        se_tr = se.xpath("//div[@class='box']//tr")
        for i in range(len(se_tr)):
            se_title = se.xpath("//div[@class='box']//tr[%d + 1]/td[3]/a/font/text()" % i).extract()
            se_url = se.xpath("//div[@class='box']//tr[%d + 1]/td[3]/a/@href" % i).extract()
            se_ctid = re.findall(re_ctid, se_url[0])
            se_qi = re.findall(re_qiid, se_title[0])
            se_create = se.xpath("//div[@class='box']//tr[%d + 1]/td[4]/a/font/text()" % i).extract()
            item = GetWenCtItem()
            item['title'] = se_title[0]
            item['qi_num'] = se_qi[0]
            item['type_id'] = 4
            item['create_by'] = se_create[0]
            item['ct_id'] = se_ctid[0]
            yield item


class GetNewCtSpider(CrawlSpider):
    name = 'get_new_ct_gao'
    download_delay = 1
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/html/gg.html', 'https://www.2m010.cc/html/gao.html']
    rules = (
        Rule(LinkExtractor(allow=(r'/html/(\d*).html')),
             callback="parse_item",
             follow=True),
        Rule(LinkExtractor(allow=(r'/plus/view.php?aid=(\d*)')),
             callback="parse_item",
             follow=True),
    )
    for url in rules:
        print(url)

    def parse_item(self, response):
        se_url = re.findall(re_ctid, response.url)
        se = Selector(response)
        se_title = se.xpath("//div[@class='display_th']/text()").extract()
        se_time = se.xpath("//div[@class='topbg clearfix']/dl/dd/b/text()").extract()
        se_time_re = re.findall(re_time, se_time[0])
        se_type = se.xpath("//div[@id='main_88lt']/div/a[2]/@href").extract()
        se_typeid = re.findall(re_typeid, se_type[0])

        se_content = se.xpath(".//div[@class='neirong']//text()").extract()
        se_img = se.xpath("//div[@class='neirong']/img/@src").extract()


        item = GetWenCtItem()

        item['title'] = se_title[0]
        item['ct_id'] = se_url[0]
        item['type_id'] = se_typeid[0]
        item['time'] = se_time_re[0]
        item['content'] = '<br />' .join(str(i) for i in se_content)
        if len(se_img) > 0:
            save_img_path = PIC_URL_SELF + se_url[0] + '.jpg'
            request.urlretrieve(se_img[0], save_img_path)
            item['img'] = se_url[0] + '.jpg'
        else:
            item['img'] = ''
        yield item


class GetNewListGaoSpider(scrapy.Spider):
    name = 'get_new_list_gao'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/html/gao.html']
    # result = datebase.query_dic({
    #     'delete': 'lt_new_list',
    #     'where': {'type_id': 117}
    # })

    def parse(self, response):
        se = Selector(response)
        se_tr = se.xpath("//table//tr")
        for i in range(len(se_tr) - 1):
            se_title = se.xpath("//table//tr[%d + 1]/td[2]/a/text()" % i).extract()
            se_url = se.xpath("//table//tr[%d + 1]/td[2]/a/@href" % i).extract()
            se_ctid = re.findall(re_ctid, se_url[0])
            if not len(se_ctid):
                se_ctid = re.findall(re_ctid2, se_url[0])
            se_qi = re.findall(re_qiid, se_title[0])
            se_create = se.xpath("//table//tr[%d + 1]/td[3]/font/text()" % i).extract()
            item = GetWenCtItem()
            item['title'] = se_title[0]
            item['qi_num'] = se_qi[0]
            item['type_id'] = 117
            item['create_by'] = se_create[0]
            item['ct_id'] = se_ctid[0]
            yield item
        pass

