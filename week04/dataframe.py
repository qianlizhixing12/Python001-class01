import pandas as pd

df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
df2 = pd.DataFrame([['a', 'b'], ['c', 'd']])
# print(df1)
# print(df2)
df2.columns = ['one', 'two']
print(df2)
df2.index = ['first', 'second']
print(df2)