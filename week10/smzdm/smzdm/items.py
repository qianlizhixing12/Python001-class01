# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmzdmPhoneItem(scrapy.Item):
    product = scrapy.Field()
    dt = scrapy.Field()
    content = scrapy.Field()
