import requests
from bs4 import BeautifulSoup as bs
from time import sleep


def getPageInfo(url):
  headers = {
      'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
  }
  response = requests.get(url, headers=headers, verify=False)
  bs_info = bs(response.text, 'html.parser')
  for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for tag in tags.find_all('a'):
      #电影详情链接
      print(tag.get('href'))
      #电影名称
      print(tag.find('span').text)


def getAllInfo():
  pageSize = 25
  urls = tuple(
      f'https://movie.douban.com/top250?start={page * pageSize}&filter='
      for page in range(10))
  for pageUrl in urls:
    getPageInfo(pageUrl)
    #降低频率防爬
    sleep(5)


getAllInfo()