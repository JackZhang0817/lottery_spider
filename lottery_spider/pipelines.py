# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
from twisted.enterprise import adbapi


class LotterySpiderPipeline(object):
    def process_item(self, item, spider):
        return item



class WebcrawlerScrapyPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',#编码要加上，否则可能出现中文乱码问题
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('mysql.connector', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)#调用插入的方法
        query.addErrback(self._handle_error, item, spider)#调用异常处理方法
        return item
    #写入数据库中
    def _conditional_insert(self, tx, item):
        #print item['name']
        sql = "insert into testtable(name,url) values(%s,%s)"
        params = (item["name"], item["url"])
        tx.execute(sql, params)

    #错误处理方法
    def _handle_error(self, failue, item, spider):
        print('--------------database operation exception!!-----------------')
        print('-------------------------------------------------------------')
        print(failue)
