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
            ma_1 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[1]/div[2]/text()" % i).extract()
            ma_2 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[2]/div[2]/text()" % i).extract()
            ma_3 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[3]/div[2]/text()" % i).extract()
            ma_4 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[4]/div[2]/text()" % i).extract()
            ma_5 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[5]/div[2]/text()" % i).extract()
            ma_6 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[6]/div[2]/text()" % i).extract()
            ping_1 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[1]/div[1]/text()" % i).extract()
            ping_2 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[2]/div[1]/text()" % i).extract()
            ping_3 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[3]/div[1]/text()" % i).extract()
            ping_4 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[4]/div[1]/text()" % i).extract()
            ping_5 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[5]/div[1]/text()" % i).extract()
            ping_6 = se.xpath("//div[@id='main']//tr[%d + 2]/td[4]/div[1]/div[6]/div[1]/text()" % i).extract()
            special_num = se.xpath("//div[@id='main']//tr[%d + 2]/td[5]/div/div[1]/text()" % i).extract()
            special_ma = se.xpath("//div[@id='main']//tr[%d + 2]/td[5]/div/div[2]/text()" % i).extract()
            single = se.xpath("//div[@id='main']//tr[%d + 2]/td[7]/text()" % i).extract()
            bo_color = se.xpath("//div[@id='main']//tr[%d + 2]/td[8]/text()" % i).extract()
            min = se.xpath("//div[@id='main']//tr[%d + 2]/td[9]/text()" % i).extract()
            five_elements = se.xpath("//div[@id='main']//tr[%d + 2]/td[10]/text()" % i).extract()
            tetou = se.xpath("//div[@id='main']//tr[%d + 2]/td[11]/text()" % i).extract()
            weishu = se.xpath("//div[@id='main']//tr[%d + 2]/td[12]/text()" % i).extract()
            hedanshuang = se.xpath("//div[@id='main']//tr[%d + 2]/td[13]/text()" % i).extract()
            jiaye = se.xpath("//div[@id='main']//tr[%d + 2]/td[14]/text()" % i).extract()
            door_num = se.xpath("//div[@id='main']//tr[%d + 2]/td[15]/text()" % i).extract()
            duan_num = se.xpath("//div[@id='main']//tr[%d + 2]/td[16]/text()" % i).extract()
            yinyang = se.xpath("//div[@id='main']//tr[%d + 2]/td[17]/text()" % i).extract()
            tiandi = se.xpath("//div[@id='main']//tr[%d + 2]/td[18]/text()" % i).extract()
            jixiong = se.xpath("//div[@id='main']//tr[%d + 2]/td[19]/text()" % i).extract()
            sexiao = se.xpath("//div[@id='main']//tr[%d + 2]/td[20]/text()" % i).extract()
            bihua = se.xpath("//div[@id='main']//tr[%d + 2]/td[21]/text()" % i).extract()
            sex = se.xpath("//div[@id='main']//tr[%d + 2]/td[22]/text()" % i).extract()
            zonghe = se.xpath("//div[@id='main']//tr[%d + 2]/td[23]/text()" % i).extract()

            item = LotteryRecordItem()
            item['create_time'] = create_time[0]
            item['qi_num'] = qi_num[0]
            item['ping_1'] = ping_1[0]
            item['ping_2'] = ping_2[0]
            item['ping_3'] = ping_3[0]
            item['ping_4'] = ping_4[0]
            item['ping_5'] = ping_5[0]
            item['ping_6'] = ping_6[0]
            item['ma_1'] = ma_1[0]
            item['ma_2'] = ma_2[0]
            item['ma_3'] = ma_3[0]
            item['ma_4'] = ma_4[0]
            item['ma_5'] = ma_5[0]
            item['ma_6'] = ma_6[0]
            item['special_ma'] = special_ma[0]
            item['special_num'] = special_num[0]
            item['single'] = single[0]
            item['bo_color'] = bo_color[0]
            item['min'] = min[0]
            item['five_elements'] = five_elements[0]
            item['tetou'] = tetou[0]
            item['weishu'] = weishu[0]
            item['hedanshuang'] = hedanshuang[0]
            item['jiaye'] = jiaye[0]
            item['door_num'] = door_num[0]
            item['duan_num'] = duan_num[0]
            item['yinyang'] = yinyang[0]
            item['tiandi'] = tiandi[0]
            item['jixiong'] = jixiong[0]
            item['sexiao'] = sexiao[0]
            item['bihua'] = bihua[0]
            item['sex'] = sex[0]
            item['zonghe'] = zonghe[0]
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


