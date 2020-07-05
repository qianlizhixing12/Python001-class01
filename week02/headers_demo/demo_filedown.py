import requests

# 下载图片
img_url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1320441599,4127074888&fm=26&gp=0.jpg'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
r = requests.get(url=img_url, headers=headers, stream=True)
with open('cap.jpg', 'wb') as img:
  for chunk in r.iter_content(chunk_size=1024):
    if chunk:
      img.write(chunk)