gen = (i for i in range(2))
print(next(gen))
print(next(gen))
try:
  print(next(gen))
except (ZeroDivisionError, StopIteration, Exception) as e:
  print('错误', e)