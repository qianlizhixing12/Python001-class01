from fake_useragent import UserAgent
import requests

with requests.Session() as s:
  ua = UserAgent(verify_ssl=False)
  headers = {
      'User-Agent':
          ua.random,
      'Referer':
          'https://accounts.douban.com/passport/login_popup?login_source=anony'
  }
  login_url = 'https://accounts.douban.com/j/mobile/login/basic'
  form_data = {
      'ck': '',
      'name': '12rf@qq.com',
      'password': 'ddd',
      'remember': 'false',
      'ticket': ''
  }
  response = s.post(login_url, data=form_data, headers=headers)
  print(response.text)
