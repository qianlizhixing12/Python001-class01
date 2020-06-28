import requests
from lxml import etree
# import lxml
import pandas as pd

demo = {
    'url': 'https://movie.douban.com/subject/1292052/',
    'headers': {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }
}
response = requests.get(demo['url'], headers=demo['headers'], verify=False)

selector = etree.HTML(response.text)
# selector = lxml.etree.HTML(response.text)
filename = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
dt = selector.xpath('//*[@id="info"]/span[10]/text()')
av = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
info = [filename, dt, av]
print(info)
movie = pd.DataFrame(data=info)
movie.to_csv('./movie.csv', encoding='utf8', index=False, header=False)