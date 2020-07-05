import requests
import os
from PIL import Image
import pytesseract

# 打开并显示文件
im = Image.open(r'cap.jpg')
im.show()

# 灰度图片
gray = im.convert('L')
gray.save('cap1.jpg')
im.close()

# 二值化
threshold = 100
table = []

for i in range(256):
  if i < threshold:
    table.append(0)
  else:
    table.append(1)

out = gray.point(table, '1')
out.save('cap2.jpg')

th = Image.open('cap2.jpg')
print(pytesseract.image_to_string(th, lang='chi_sim+eng'))
