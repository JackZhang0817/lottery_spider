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
    def __init__(self):
        self.data_mysql = MySQL()

    def open_spider(self, spider):
        if spider.name == 'get_freedata_page':
            database = MySQL()
            result = database.query_dic({
                'delete': 'lt_freedata_list',
                'where': {'update_time': "''"}
            })
            print(result)
        elif spider.name == 'get_new_list':
            result = self.data_mysql.query_dic({
                'delete': 'lt_new_list',
                'where': {'type_id': 4}
            })
            print(result)
        elif spider.name == 'get_new_list_gao':
            result = self.data_mysql.query_dic({
                'delete': 'lt_new_list',
                'where': {'type_id': 117}
            })
            print(result)

    def process_item(self, item, spider):
        if spider.name == 'lottery_records' or spider.name == 'lottery_record2':
            self.pip_lottery(item)
        elif spider.name == 'get_wen_list' or spider.name == 'get_title_name':
            self.pip_wen_list(item)
        elif spider.name == 'get_zonglist' or spider.name == 'get_single_page':
            self.pip_zi_ct(item)
        elif spider.name == 'get_zilist':
            self.pip_zi2_ct(item)
        elif spider.name == 'get_new_list' or spider.name == 'get_new_list_gao':
            self.pip_new_list(item)
        elif spider.name == 'get_new_ct' or spider.name == 'get_new_ct_gao':
            self.pip_new_ct(item)
        elif spider.name == 'get_picture_list':
            self.pip_pic_list(item)
        elif spider.name == 'get_freedata_page':
            self.pip_freedata_list(item)
        elif spider.name == 'get_typelist':
            self.pip_zi_ct(item)
        return item

    def pip_lottery(self, item):
        datebase = MySQL()
        item["create_time"] = self.handle_timesamp(item['create_time'])
        result2 = datebase.query_dic({
            'insert': 'lt_record',
            'domain_array': [
                'create_time', 'time', 'qi_num', 'ping_1', 'ping_2', 'ping_3', 'ping_4', 'ping_5', 'ping_6', 'ma_1', 'ma_2', 'ma_3', 'ma_4', 'ma_5', 'ma_6', 'se_1', 'se_2', 'se_3', 'se_4', 'se_5', 'se_6', 'special_ma', 'special_num', 'special_color', 'single', 'bo_color', 'min', 'five_elements', 'tetou', 'weishu', 'hedanshuang', 'jiaye', 'door_num', 'duan_num', 'yinyang', 'tiandi', 'jixiong', 'heibai', 'sexiao', 'bihua', 'sex', 'zonghe',
            ],
            'value_array': [
                item["create_time"], item['time'], item['qi_num'], item['ping_1'], item['ping_2'], item['ping_3'], item['ping_4'], item['ping_5'], item['ping_6'], item['ma_1'], item['ma_2'], item['ma_3'], item['ma_4'], item['ma_5'], item['ma_6'], item['se_1'], item['se_2'], item['se_3'], item['se_4'], item['se_5'], item['se_6'], item['special_ma'], item['special_num'],  item['special_color'], item['single'], item['bo_color'], item['min'], item['five_elements'], item['tetou'], item['weishu'], item['hedanshuang'], item['jiaye'], item['door_num'], item['duan_num'], item['yinyang'], item['tiandi'], item['jixiong'], item['heibai'], item['sexiao'], item['bihua'], item['sex'], item['zonghe'],
            ]
        })
        return result2

    def pip_wen_list(self, item):
        datebase = MySQL()
        item['time'] = int(time.time())

        result2 = datebase.query_dic({
            'insert': 'lt_wen_list',
            'domain_array': [
                'title', 'type_id', 'create_time'
            ],
            'value_array': [
                item["title"], item["type_id"], item["time"]
            ]
        })
        return result2

    def pip_zi_ct(self, item):
        datebase = MySQL()
        item['create_time'] = int(time.time())
        # item['time'] = self.handle_timesamp(item['time'])

        result2 = datebase.query_dic({
            'insert': 'lt_type_list',
            'domain_array': [
                'ct_id', 'type_id', 'title', 'time', 'abstract', 'create_time'
            ],
            'value_array': [
                item["ct_id"], item["type_id"], item["title"], item["time"], item["abstract"], item["create_time"]
            ]
        })
        return result2

    def pip_new_list(self, item):
        datebase = MySQL()
        item['create_time'] = int(time.time())
        result2 = datebase.query_dic({
            'insert': 'lt_new_list',
            'domain_array': [
                'ct_id', 'type_id', 'title', 'qi_num', 'create_by', 'create_time'
            ],
            'value_array': [
                item["ct_id"], item["type_id"], item["title"], item["qi_num"], item["create_by"], item["create_time"]
            ]
        })
        return result2


    def pip_pic_list(self, item):
        datebase = MySQL()
        item['create_time'] = int(time.time())
        result2 = datebase.query_dic({
            'update': 'lt_picture',
            'value_array': {
                'title': item['pic_title'],
                'qishu': item['pic_qi_num'],
                'thumb': item['pic_thumb_url']
            },
            'where': {'col_id': item['pic_ct_id'], 'year': item['pic_year']}
        })
        return result2

    def pip_freedata_list(self, item):
        datebase = MySQL()
        item['create_time'] = int(time.time())
        # item['time'] = self.handle_timesamp(item['time'])

        result2 = datebase.query_dic({
            'insert': 'lt_freedata_list',
            'domain_array': [
                'type_id', 'title', 'create_time'
            ],
            'value_array': [
                item["type_id"], item["title"], item["create_time"]
            ]
        })
        return result2


    def pip_zi2_ct(self, item):
        datebase = MySQL()
        item['update_time'] = int(time.time())
        result = datebase.query_dic({
            'update': 'lt_type_list',
            'value_array': {
                'content': item['content'],
                'img': item['img'],
                'update_time': item['update_time']
            },
            'where': {'ct_id': item['ct_id']}
        })
        return result

    def pip_new_ct(self, item):
        datebase = MySQL()
        item['update_time'] = int(time.time())
        item['time'] = self.handle_timesamp(item['time'], 1)
        result = datebase.query_dic({
            'update': 'lt_new_list',
            'value_array': {
                'content': item['content'],
                'img': item['img'],
                'time': item['time'],
                'update_time': item['update_time']
            },
            'where': {'ct_id': item['ct_id']}
        })
        return result
    '''
    处理时间, 处理成为时间戳
    '''

    def handle_timesamp(self, dt, state=0):
        if state == 0:
            time_arr = time.strptime(dt, "%Y-%m-%d")
        elif state == 1:
            time_arr = time.strptime(dt, "%Y-%m-%d %H:%M")
        time_samp = int(time.mktime(time_arr))
        return time_samp



