# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import GetWenCtItem
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib import request
from lottery_spider.settings import PIC_URL_SELF

import re
import time

re_url = r'/html/(\d*).html'
re_typeid = r'(\d*)_\d*.html'
re_time = r'.*?：(.*?$)'

class GetZilistSpider(CrawlSpider):
    name = 'get_zilist'
    # name = 'get_typelist'
    # name = 'get_title_name'
    download_delay = 1
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/', 'http://www.2m010.cc/html/ziliao.html', 'https://www.2m010.cc/html/266_1.html', 'https://www.2m010.cc/html/241_1.html', 'https://www.2m010.cc/html/240_1.html', 'https://www.2m010.cc/html/243_1.html', 'https://www.2m010.cc/html/177_1.html', 'https://www.2m010.cc/html/239_1.html']
    # start_urls = ['https://www.2m010.cc/html/253672.html']
    if name == 'get_title_name':
        rules = (
            Rule(LinkExtractor(allow=(r'/html/(\d*)_1.html')),
                 callback="parse_title",
                 follow=True),
         )
    elif name == 'get_zilist':
        rules = (
            # Rule(LinkExtractor(allow=(r'/html/(\d*)_([1|2]).html')),
            #      callback="parse_list",
            #      follow=True),
            Rule(LinkExtractor(allow=(r'/html/(\d*)_(\d+).html'))),
            Rule(LinkExtractor(allow=(r'/html/(\d*).html')),
                 callback="parse_item",
                 follow=True),
        )
    else:
        rules = (
            Rule(LinkExtractor(allow=(r'/html/(\d*)_([1|2]).html')),
                 callback="parse_list",
                 follow=True),
            # Rule(LinkExtractor(allow=(r'/html/(\d*)_([1|2]).html'))),
            # Rule(LinkExtractor(allow=(r'/html/(\d*).html')),
            #      callback="parse_item",
            #      follow=True),
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
        #     save_img_path = PIC_URL_SELF + se_url[0] + '.jpg'
        #     request.urlretrieve(se_img[0], save_img_path)
            item['img'] = se_img[0]
        else:
            item['img'] = ''
        yield item


    def parse_title(self, response):
        se_url = re.findall(re_typeid, response.url)
        se = Selector(response)
        item = GetWenCtItem()
        se_title = se.xpath("//div[@class='place']/a[3]/text()").extract()
        if len(se_title) < 1:
            se_title = se.xpath("//div[@class='place']/a[2]/text()").extract()
        item['type_id'] = se_url[0]
        item['title'] = se_title[0]
        yield item




    def parse_list(self, response):
        se_url = re.findall(re_typeid, response.url)
        se = Selector(response)
        se_li = se.xpath("//div[@class='listbox']/ul/li")

        for i in range(len(se_li)):
            se_title = se.xpath("//div[@class='listbox']/ul/li[%d + 1]/a/text()" % i).extract()
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
        pass


class GetZongListSpider(CrawlSpider):
    name = 'get_zonglist'
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/', 'http://www.2m010.cc/html/ziliao']
    # start_urls = ['https://www.2m010.cc/html/240_1.html']
    # start_urls = ['https://www.2m010.cc/html/253672.html']
    rules = (
        Rule(LinkExtractor(allow=(r'/html/(\d*)_([1|2]).html')),
             callback="parse_editor",
             follow=True),
        # Rule(LinkExtractor(allow=(r'/html/328_1.html')),
        #      callback="parse_editor",
        #      follow=True),
        # Rule(LinkExtractor(allow=(r'/html/(\d*).html')),
        #      callback="parse_item",
        #      follow=True),
    )
    for rule in rules:
        print(rule)

    def parse_editor(self, response):
        se_url = re.findall(re_typeid, response.url)
        se = Selector(response)
        se_li = se.xpath("//div[@class='listbox']/ul/li")

        for i in range(len(se_li)):
            se_title = se.xpath("//div[@class='listbox']/ul/li[%d + 1]/a/text()" % i).extract()
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


class GetNewsListSpider(CrawlSpider):
    name = 'get_news_list'
    download_delay = 1
    allowed_domains = ['www.2m010.cc']
    start_urls = ['https://www.2m010.cc/html/21555.html']
    # start_urls = ['https://www.2m010.cc/html/253672.html']
    rules = (
        Rule(LinkExtractor(allow=(r'/html/4_1.html')),
             callback="parse_item",
             follow=True),
        # Rule(LinkExtractor(allow=(r'/html/(\d*).html')),
        #      callback="parse_item",
        #      follow=True),
    )
    print(rules)
    for rule in rules:
        print('rrr')
        print(rule)

    def parse_item(self, response):
        url = response.url
        se_type = re.findall(re_typeid, url)
        se = Selector(response)
        se_tr = se.xpath("//table/tbody/tr")

        for i in range(len(se_tr)):
            se_title = se.xpath("//table/tbody/tr[%d + 1]/td[2]/text()").extract()
            se_create_by = se.xpath("//table/tbody/tr[%d +1]/td[3]/text()").extract()
            item = GetWenCtItem()
            item['title'] = se_title
            item['create_time'] = se_create_by
            item['type_id'] = se_type
            yield item


    '''
    def parse(self, response):
        se = Selector(response)
        se_tr = se.xpath("//div[@class='listbox']/ul/li").extract()[0]
        item = GetCollectItem()
        item['content'] = se_tr
        yield item
        pass
    '''
