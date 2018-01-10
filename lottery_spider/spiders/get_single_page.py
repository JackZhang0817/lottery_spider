# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from urllib import request
from lottery_spider.items import GetWenCtItem
from lottery_spider.items import GetFreeDataItem
import re
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib import request
from lottery_spider.settings import PIC_URL_SELF


re_url = r'/html/(\d*).html'
re_typeid = r'(\d*)_\d*.html'
re_time = r'.*?：(.*?$)'


class GetSinglePageSpider(scrapy.Spider):
    name = 'get_single_page'
    # str = input('请输入拉取单页的ID：')
    str = '239'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['http://2m010.cc/html/' + str + '_1.html']

    def parse(self, response):
        se_url = re.findall(re_typeid, response.url)
        se = Selector(response)
        se_li = se.xpath("//div[@class='listbox']/ul/li")

        for i in range(len(se_li)):
            se_title = se.xpath("//div[@class='listbox']/ul/li[%d + 1]/a/text()" % i).extract()
            if len(se_title) < 1:
                se_title = se.xpath("//div[@class='listbox']/ul/li[%d + 1]/a/b/text()" % i).extract()
            se_a = se.xpath("//div[@class='listbox']/ul/li[%d + 1]/a/@href" % i).extract()
            ct_id = re.findall(re_url, se_a[0])
            se_time = se.xpath("//div[@class='listbox']/ul/li[%d + 1]/span/text()" % i).extract()
            se_abstract = se.xpath("//div[@class='listbox']/ul/li[%d + 1]/p/text()" % i).extract()
            item = GetWenCtItem()
            item['ct_id'] = ct_id[0]
            item['type_id'] = se_url[0]
            item['title'] = se_title[0]
            item['time'] = self.handle_timesamp(se_time[1])
            item['abstract'] = se_abstract[0]
            yield item

    def handle_timesamp(self, dt):
        time_arr = time.strptime(dt, "%Y-%m-%d %H:%M:%S ")
        time_samp = int(time.mktime(time_arr))
        return time_samp


class GetPageContent(CrawlSpider):
    name = 'get_single_page_ct'
    str = '1'
    download_delay = 1
    allowed_domains = ['www.2m010.cc']
    # str = input('请输入拉取单页的ID：')
    start_urls = ['https://www.2m010.cc/html/' + str + '_1.html']
    # start_urls = ['https://www.2m010.cc/html/253672.html']
    rules = (
        Rule(LinkExtractor(allow=(r'/html/71_([1|2]).html'))),
        Rule(LinkExtractor(allow=(r'/html/(\d*).html')),
             callback="parse_item",
             follow=True),
    )
    for rule in rules:
        print(rule)

    def parse_item(self, response):
        se_url = re.findall(re_url, response.url)
        se = Selector(response)
        se_title = se.xpath("//div[@class='display_th']/text()").extract()
        se_time = se.xpath("//div[@class='topbg clearfix']/dl/dd/b/text()").extract()
        se_time_re = re.findall(re_time,se_time[0])
        se_type = se.xpath("//div[@id='main_88lt']/div/a[2]/@href").extract()
        se_typeid = re.findall(re_typeid, se_type[0])

        se_content = se.xpath(".//div[@class='neirong']/text()").extract()
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


class GetFreeDataSpider(scrapy.Spider):
    name = 'get_freedata_page'
    # str = input('请输入拉取单页的ID：')
    allowed_domains = ['www.2m010.cc']
    start_urls = ['http://www.2m010.cc/']

    def parse(self, response):
        se_url = re.findall(re_typeid, response.url)
        se = Selector(response)
        se_li = se.xpath("//div[@class='ycgs_box_inner ulleft']/ul/li")

        for i in range(len(se_li)):
            se_title = se.xpath("//div[@class='ycgs_box_inner ulleft']/ul/li[%d + 1]/a/text()" % i).extract()
            se_a = se.xpath("//div[@class='ycgs_box_inner ulleft']/ul/li[%d + 1]/a/@href" % i).extract()
            type_id = re.findall(re_typeid, se_a[0])
            item = GetFreeDataItem()
            item['type_id'] = type_id[0]
            item['title'] = se_title[0]
            yield item

    def handle_timesamp(self, dt):
        time_arr = time.strptime(dt, "%Y-%m-%d %H:%M:%S ")
        time_samp = int(time.mktime(time_arr))
        return time_samp
