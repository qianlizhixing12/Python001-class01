import pretty_errors

f = open('a.txt', encoding='utf8')
try:
  data = f.read()
finally:
  f.close()

with open('a.txt', encoding='utf8') as f1:
  data1 = f1.read()