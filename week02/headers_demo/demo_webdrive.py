from selenium import webdriver
import time

try:
  bs = webdriver.Chrome()

  #登录模拟
  bs.get('https://www.douban.com')
  time.sleep(1)
  bs.switch_to_frame(bs.find_elements_by_tag_name('iframe')[0])
  bs.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
  bs.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
  bs.find_element_by_xpath('//*[@id="password"]').send_keys('test123test456')
  time.sleep(1)
  bs.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()
  time.sleep(1)
  cookies = bs.get_cookies()  # 获取cookies
  print(cookies)

  #获取评论
  bs.get('https://movie.douban.com/subject/1292052/')
  time.sleep(1)
  bs.find_element_by_xpath('//*[@id="hot-comments"]/a').click()

except Exception as identifier:
  pass
finally:
  bs.close()