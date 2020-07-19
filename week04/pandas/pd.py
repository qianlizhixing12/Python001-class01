import numpy as np
import pandas as pd
import matplotlib as plt
import os

pwd = os.path.dirname(os.path.realpath(__file__))
book = os.path.join(pwd, 'book_utf8.csv')
df = pd.read_csv(book)
# print(df)
# print(df['还行'])
df.columns = ['star', 'vote', 'shorts']
# print(df.loc[0:3, ['star']])
# print(df['star'] == '力荐')
# print(df[df['star'] == '力荐'])
# print(df)
df.dropna()
# print(df.groupby('star').sum())
star_to_number = {'力荐': 5, '推荐': 4, '还行': 3, '较差': 2, '很差': 1}
df['new_star'] = df['star'].map(star_to_number)
print(df)
