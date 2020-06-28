import scrapy
from homework2.items import MovieItem


class MoviesSpider(scrapy.Spider):
  name = 'movies'
  allowed_domains = ['maoyan.com']
  start_urls = ['https://maoyan.com/films?showType=3']

  def start_requests(self):
    url = 'https://maoyan.com/films?showType=3'
    yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    for link in scrapy.Selector(response=response).xpath(
        '//div[contains(@class, "movie-item film-channel") and position() < 11]/a[1]/@href'
    ):
      yield scrapy.Request(url='https://maoyan.com' + link.extract(),
                           callback=self.parseDetail)

  def parseDetail(self, response):
    item = MovieItem()
    selector = scrapy.Selector(response=response)
    item['name'] = selector.xpath(
        '//div[@class="movie-brief-container"]/h1[1]/text()').extract_first()
    item['style'] = ''.join(
        selector.xpath('//a[@class="text-link"]/text()').extract())
    item['dt'] = selector.xpath(
        '//li[@class="ellipsis"][3]/text()').extract_first()
    yield item