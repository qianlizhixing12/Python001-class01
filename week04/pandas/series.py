import pandas as pd
import numpy as np

s = pd.Series(['a', 'b', 'c'])
# print(s)
s1 = pd.Series({'a': 11, 'b': 22, 'c': 33})
# print(s1)
s2 = pd.Series([11, 22, 33], index=['a', 'b', 'c'])
# print(s2)
# print(s1.index)
# print(s1.values)

emails = pd.Series(
    ['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
import re
pattern = '[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
print(emails[mask])