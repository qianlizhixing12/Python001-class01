import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep


def getInfo(url):
  headers = {
      'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
      'Cookie':
          '__mta=45576603.1593186094936.1593343238155.1593346877994.15; uuid_n_v=v1; uuid=7FF6FC20B7C311EA9B3075693A212BAF7030C18987AF40C7A51DD03BF133BE66; _lxsdk_cuid=172f14a8c04c8-03278cd035a66d-4353760-100200-172f14a8c04c8; _lxsdk=7FF6FC20B7C311EA9B3075693A212BAF7030C18987AF40C7A51DD03BF133BE66; mojo-uuid=f8e70e70bb2a45bc2423eafaa2c52a24; _csrf=e16e101895d2382732a70f854131d773e8b4b9fe47752849b0eeeadc844efe3b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593187599,1593187741,1593228471,1593343233; mojo-session-id={"id":"e027243f5706553f73bbfe802b6087fc","time":1593352758898}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593352774; __mta=45576603.1593186094936.1593346877994.1593352774278.16; _lxsdk_s=172fb397caa-05a-c56-957%7C%7C5'
  }
  response = requests.get(url, headers=headers, verify=False)
  return response.text


def getMovieInfo(url):
  info = []
  response = getInfo(url)
  bs_info = bs(response, 'html.parser')
  for tags in bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
    # 电影名称
    name = tags.find('h1', attrs={'class': 'name'}).text
    info.append(name)
    #电影类型
    style = ''.join(
        tag.text for tag in tags.find_all('a', attrs={'class': 'text-link'}))
    info.append(style)
    #上映时间
    dt = tags.find_all('li', attrs={'class': 'ellipsis'})[-1].text
    info.append(dt)
  return info


def getAllUrl():
  urls = []
  response = getInfo('https://maoyan.com/films?showType=3')
  bs_info = bs(response, 'html.parser')
  for tag in bs_info.find_all('div',
                              attrs={'class': 'movie-item film-channel'},
                              limit=10):
    urls.append('https://maoyan.com' +
                tag.find('a', attrs={
                    'data-act': 'movie-click'
                }).get('href'))
  return urls


def getMovies():
  infos = []
  for url in getAllUrl():
    infos.append(getMovieInfo(url))
    #降低频率防爬
    sleep(5)
  pd.DataFrame(data=infos).to_csv('./week01/movies.csv',
                                  encoding='utf8',
                                  index=False,
                                  header=False)


getMovies()