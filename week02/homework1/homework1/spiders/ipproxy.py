import scrapy
from homework1.items import MovieItem


class IpproxySpider(scrapy.Spider):
  name = 'ipproxy'
  allowed_domains = ['maoyan.com']
  start_urls = ['https://maoyan.com/films?showType=3']

  def parse(self, response):
    for selector in scrapy.Selector(response=response).xpath(
        '//div[@class="movie-hover-info" and position() < 11]'):
      item = MovieItem()
      item['name'] = selector.xpath('div[1]/@title').extract_first().strip()
      item['style'] = selector.xpath('div[2]/text()[2]').extract_first().strip()
      item['dt'] = selector.xpath('div[4]/text()[2]').extract_first().strip()
      yield item
