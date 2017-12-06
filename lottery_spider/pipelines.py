# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
from twisted.enterprise import adbapi
import aiomysql


class LotterySpiderPipeline(object):
    def process_item(self, item, spider):
        return item



class LotteryRecordPipeline(object):
    def process_item(self, item, spider):
        conn = mysql.connector.connect(host='192.168.1.108', user='root', password='ling123', database='lottery_sql')
        cursor = conn.cursor()
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        cursor.commit()
        cursor.close()
        return item
