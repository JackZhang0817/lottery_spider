# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import sys
# sys.path.append('e:\HomeProject\Python\lottery_spider\database.py')

from database import MySQL
import time


class LotterySpiderPipeline(object):
    def process_item(self, item, spider):
        return item



class LotteryRecordPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'lottery_record':
            self.pip_lottery(item)
        return item

    def pip_lottery(self, item):
        datebase = MySQL()

        item["create_time"] = self.handle_timesamp(item['create_time'])

        result2 = datebase.query_dic({
            'insert': 'lt_record',
            'domain_array': [
                'create_time', 'qi_num', 'ping_1', 'ping_2', 'ping_3', 'ping_4', 'ping_5', 'ping_6', 'ma_1', 'ma_2', 'ma_3', 'ma_4', 'ma_5', 'ma_6', 'special_ma', 'special_num', 'single', 'bo_color', 'min', 'five_elements', 'tetou', 'weishu', 'hedanshuang', 'jiaye', 'door_num', 'duan_num', 'yinyang', 'tiandi', 'jixiong', 'sexiao', 'bihua', 'sex', 'zonghe',
            ],
            'value_array': [
                item["create_time"], item['qi_num'], item['ping_1'], item['ping_2'], item['ping_3'], item['ping_4'], item['ping_5'], item['ping_6'], item['ma_1'], item['ma_2'], item['ma_3'], item['ma_4'], item['ma_5'], item['ma_6'], item['special_ma'], item['special_num'], item['single'], item['bo_color'], item['min'], item['five_elements'], item['tetou'], item['weishu'], item['hedanshuang'], item['jiaye'], item['door_num'], item['duan_num'], item['yinyang'], item['tiandi'], item['jixiong'], item['sexiao'], item['bihua'], item['sex'], item['zonghe'],
            ]
        })
        return result2

    '''
    处理时间, 处理成为时间戳
    '''
    def handle_timesamp(self,dt):
        time_arr = time.strptime(dt, "%Y-%m-%d")
        time_samp = int(time.mktime(time_arr))
        return time_samp



