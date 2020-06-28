# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MoviePipeline:

  def process_item(self, item, spider):
    self.items.append([item['name'], item['style'], item['dt']])
    return item

  def open_spider(self, spider):
    self.items = []

  def close_spider(self, spider):
    movie = pd.DataFrame(data=self.items)
    movie.to_csv('./movie.csv', encoding='utf8', index=False, header=False)