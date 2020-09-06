# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
from snownlp import SnowNLP
from scrapy.utils.project import get_project_settings
import pymysql
import datetime


class SmzdmPhonePipeline:

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def open_spider(self, spider):
        self.items = []
        config = get_project_settings().get('MYSQL_CONFIG')
        self.conn = pymysql.connect(**config)
        self.insert = self.conn.cursor()

    def close_spider(self, spider):

        def analyze():
            #评论有空值，过滤掉
            # data = pd.DataFrame(data=self.items)
            # data = data.dropna(axis=0, subset=['content'])
            datas = filter(lambda item: item['content'].strip(), self.items)
            #情感分析SnowNLP,得分越高越正向
            updatedt = str(datetime.datetime.now().date())
            return ((
                item['product'],
                item['dt'],
                item['content'],
                SnowNLP(item['content']).sentiments,
                updatedt,
            ) for item in datas)

        try:
            datas = analyze()
            # 执行批量插入
            self.insert.executemany(
                'insert into smzdm_phone (product, dt, content, sentiments, updatedt) value (%s, %s, %s, %s, %s)',
                datas)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.insert.close()
            self.conn.close()
