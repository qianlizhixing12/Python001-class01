import scrapy
from bs4 import BeautifulSoup as bs
from crawi_scrapy.items import MovieItem


class MoviesSpider(scrapy.Spider):
  name = 'movies'
  allowed_domains = ['movie.douban.com']
  start_urls = ['https://movie.douban.com/top250']

  def start_requests(self):
    pageSize = 25
    for page in range(10):
      url = f'https://movie.douban.com/top250?start={page * pageSize}&filter='
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    soup = bs(response.text, 'html.parser')
    for tags in soup.find_all('div', attrs={'class': 'hd'}):
      item = MovieItem()
      #电影名称
      title = tags.find('a').find('span').text
      #电影详情链接
      link = tags.find('a').get('href')
      item['title'] = title
      item['link'] = link
      yield scrapy.Request(url=link, meta=item, callback=self.parseDetail)

  def parseDetail(self, response):
    item = response.meta
    soup = bs(response.text, 'html.parser')
    #电影详情评论
    content = soup.find('div', attrs={
        'class': 'related-info'
    }).get_text().strip()
    item['content'] = content
    yield item