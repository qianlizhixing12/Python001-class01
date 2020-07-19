import pandas as pd

excel1 = pd.read_excel(r'1.xlsx')
print(excel1)

import pymysql
sql = 'SELECT *  FROM mytable'
conn = pymysql.connect('ip', 'name', 'pass', 'dbname', 'charset=utf8')
df = pd.read_sql(sql, conn)
