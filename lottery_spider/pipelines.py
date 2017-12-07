# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import sys
# sys.path.append('e:\HomeProject\Python\lottery_spider\database.py')

from database import MySQL


class LotterySpiderPipeline(object):
    def process_item(self, item, spider):
        return item



class LotteryRecordPipeline(object):
    def process_item(self, item, spider):
        datebase = MySQL()
        result2 = datebase.query_dic({
            'insert': 'user',
            'domain_array': [
                'name',
            ],
            'value_array': [
                item["create_time"]
            ]
        })
        print(spider.name)
        print(item["create_time"])
        return item
