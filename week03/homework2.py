#coding:utf-8
from concurrent.futures import ThreadPoolExecutor
import requests
from time import sleep
import json
import pymysql
import collections
import matplotlib.pyplot as plt
# from pyecharts.charts import Pie

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def exec():
  items = (
      (city, page) for city in ('北京', '上海', '广州', '深圳') for page in range(1, 2))

  t = ThreadPoolExecutor(max_workers=4)
  result = list(t.map(execCrawi, items))
  # print(result)

  saveData(result)


def execCrawi(value):
  city, page = value

  headers = {
      'user-agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
      'accept':
          'application/json, text/javascript, */*; q=0.01',
      'accept-encoding':
          'gzip, deflate, br',
      'accept-language':
          'en-US,en;q=0.9',
      'content-type':
          'application/x-www-form-urlencoded; charset=UTF-8',
      'cookie':
          'user_trace_token=20200715221809-f117b2d2-bff4-4bab-b213-a5bc3cf01985; X_MIDDLE_TOKEN=80706bb85d1aa33b65a72a2d017c8ef2; JSESSIONID=ABAAABAABAGABFAFE0ADF2E00358FD3178FA7B72EED4600; WEBTJ-ID=07152020%2C221813-17352d710be35d-0246da4ed3a4ac-4353760-1049088-17352d710bf9d; _ga=GA1.2.1478870745.1594822693; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594822693; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217352d711c4b98-06c5725a278807-4353760-1049088-17352d711c5b35%22%2C%22%24device_id%22%3A%2217352d711c4b98-06c5725a278807-4353760-1049088-17352d711c5b35%22%7D; sajssdk_2015_cross_new_user=1; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5FPython%3Fpx%3Ddefault%26gx%3D%25E5%2585%25A8%25E8%2581%258C%26city%3D%25E5%258C%2597%25E4%25BA%25AC; _gid=GA1.2.2032967751.1594822693; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist%5FPython%253Fpx%253Ddefault%2526gx%253D%2525E5%252585%2525A8%2525E8%252581%25258C%2526city%253D%2525E5%25258C%252597%2525E4%2525BA%2525AC; LGUID=20200715221814-4252c572-e97c-4b08-9772-6b964902a3c2; LGSID=20200715221814-9fc57b11-fefd-47e2-949e-b5c1e82a3abe; index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=ca2756d8f20c403fb5f9da16ad0a5011; X_HTTP_TOKEN=e59cf452bd8a322f4072284951daa4a58726dfe560; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594822704; LGRID=20200715221824-d9749467-f040-446a-a638-c5b573bb5a99',
      'referer':
          'https://www.lagou.com/jobs/list_python%E5%B7%A5%E7%A8%8B%E5%B8%88/p-city_2?px=default',
  }
  url = f'https://www.lagou.com/jobs/positionAjax.json?px=new&gx=全职&city={city}&needAddtionalResult=false'
  data = {'first': 'false', 'pn': page, 'kd': 'Python'}

  sleep(5)
  return requests.post(url=url, data=data, headers=headers, verify=False).text


def saveData(data):
  items = convertData(data)
  saveDb(items)
  saveImg(items)


def convertData(data):
  items = []
  for s in data:
    v = json.loads(s)
    if ('success' in v) and v['success']:
      for item in v['content']['positionResult']['result']:
        items.append([
            item['city'], item['positionName'], item['salary'], item['workYear']
        ])
  return items


def saveDb(items):
  conn = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='nxx4545GGB46_fdg',
                         database='test',
                         charset='gb2312')
  qry = conn.cursor()
  try:
    # 执行批量插入
    qry.executemany(
        'insert into python_salary (city, name, salary, year) value (%s, %s, %s, %s)',
        items)
    conn.commit()
  except:
    conn.rollback()
  finally:
    qry.close()
    conn.close()


def saveImg(items):
  dic = collections.defaultdict(list)
  #解析薪资，取区间平均值
  for item in items:
    salary = item[2]
    salary = list(map(int, salary.replace('k', '000').split('-')))
    salary = sum(salary) / len(salary)
    dic[item[0]].append(salary)
  #画图1
  city, salarys = list(dic.keys()), list(dic.values())
  salarys = list(sum(salary) // len(salary) for salary in salarys)
  #饼图
  # plt.pie(salarys, labels=city, autopct='%1.1f%%', shadow=True, startangle=150)
  # plt.savefig('salary1.png')
  # plt.show()
  #柱状图
  plt.bar(city, salarys, color='rgbc')
  plt.savefig('salary.png')
  plt.show()
  #画图2
  # for key in dic:
  #   dic[key] = sum(dic[key]) / len(dic[key])
  # pie = Pie({'page_title': '北上广深最新python工作薪资'})
  # pie.add(series_name='薪资', data_pair=dic)
  # pie.render()


if __name__ == '__main__':
  exec()