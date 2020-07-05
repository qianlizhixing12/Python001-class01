from selenium import webdriver
import time
from fake_useragent import UserAgent

try:
  bs = webdriver.Chrome()

  #登录模拟
  bs.get('https://shimo.im/welcome')
  time.sleep(1)
  bs.find_element_by_xpath(
      '//button[@class="login-button btn_hover_style_8"]').click()
  time.sleep(1)
  bs.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys(
      '15055495@qq.com')
  bs.find_element_by_xpath('//input[@name="password"]').send_keys(
      'test123test456')
  time.sleep(1)
  bs.find_element_by_xpath(
      '//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()
  time.sleep(1)
  cookies = bs.get_cookies()  # 获取cookies
  sessionStorage = bs.execute_script('return sessionStorage;')
  localStorage = bs.execute_script('return localStorage;')
  print(cookies)
  print(sessionStorage)
  print(localStorage)
except Exception as identifier:
  pass
finally:
  bs.close()