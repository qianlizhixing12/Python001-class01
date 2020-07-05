# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class MoviePipeline:

  def process_item(self, item, spider):
    try:
      # 单条提交
      self.insert.execute(
          'insert into movies (name, style, dt) value (%s, %s, %s)',
          (item['name'], item['style'], item['dt']))
      self.conn.commit()
    except:
      self.conn.rollback()

    # self.items.append((item['name'], item['style'], item['dt']))
    return item

  def open_spider(self, spider):
    # self.items = []
    # , 字符编码报错‘泰囧’
    self.conn = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='nxx4545GGB46_fdg',
                                database='test',
                                charset='gb2312')
    self.insert = self.conn.cursor()
    self.query = self.conn.cursor()

  def close_spider(self, spider):
    # try:
    #   # 执行批量插入
    #   self.insert.executemany(
    #       'insert into movies (name, style, dt) value (%s, %s, %s)',
    #       tuple(self.items))
    #   self.conn.commit()
    # except:
    #   self.conn.rollback()
    # 操作的行数
    print(self.query.execute('select * from movies'))
    # 获得一条查询结果
    print(self.query.fetchone())
    # 获得所有查询结果
    print(self.query.fetchall())
    self.query.close()
    self.insert.close()
    self.conn.close()