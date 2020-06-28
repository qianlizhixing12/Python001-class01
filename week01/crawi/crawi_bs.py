import requests
from bs4 import BeautifulSoup as bs

demo = {
    'url': 'https://movie.douban.com/top250',
    'headers': {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }
}
response = requests.get(demo['url'], headers=demo['headers'], verify=False)

bs_info = bs(response.text, 'html.parser')
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
  for tag in tags.find_all('a'):
    print(tag.get('href'))
    print(tag.find('span').text)