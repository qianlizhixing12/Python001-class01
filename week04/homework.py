import pandas as pd
import pymysql


def read_data():
  '''
  SELECT * FROM data
  pandas的read_xxx加载数据
  '''
  con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='nxx4545GGB46_fdg',
                        database='test',
                        charset='gb2312')
  sql = 'select city, name, salary, year from python_salary'
  return pd.read_sql(sql, con)


def sel_row_data(data):
  '''
  SELECT * FROM data LIMIT 10
  获取部分数据 loc或iloc,和python切片stop范围不同，包括stop
  '''
  #以下方法皆可
  # return data.loc[:9]
  return data[:10]


def sel_col_data(data):
  '''
  SELECT id FROM data;  //id 是 data 表的特定一列
  同sel_col_data
  '''
  #以下方法皆可
  # return data.loc[:, 'city']
  # return data.loc[:, ['city']]
  return data['city']


def count_col_data(data):
  '''
  SELECT COUNT(id) FROM data
  count
  '''
  return data['city'].count()


def filter_data(data):
  '''
  SELECT * FROM data WHERE id<1000 AND age>30;
  data[[True, False]]
  '''
  # return data[data['city'] == '北京'][data['name'] == 'python开发工程师']
  return data[(data['city'] == '北京') & (data['name'] == 'python开发工程师')]


def group_count_data(data):
  '''
  SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
  '''
  return data.groupby('city').name.nunique()


def merge_data(df1, df2):
  '''
  SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
  merge inner默认
  '''
  return pd.merge(df1, df2, how='inner', on='id')


def concat_data(df1, df2):
  '''
  SELECT * FROM table1 UNION SELECT * FROM table2;
  concat
  '''
  return pd.concat([df1, df2])


def delete_row_data(data):
  '''
  DELETE FROM table1 WHERE id=10;
  drop
  '''
  # return data[data['age'] < 18] #返回删除的数据
  return data.drop(index=data[data['age'] < 18].index[0])


def delete_col_data(data):
  '''
  ALTER TABLE table1 DROP COLUMN column_name;
  '''
  # return data.drop(labels='age', axis=1)
  return data.drop(columns='age')


if __name__ == '__main__':
  #以week03 homework2 python薪资爬取结果作为数据源
  data = read_data()
  print(data)
  print(sel_row_data(data))
  print(sel_col_data(data))
  print(count_col_data(data))
  print(filter_data(data))
  print(group_count_data(data))
  df1 = pd.DataFrame({"id": [5, 3], "name": ['nxx', 'ngg'], "age": [14, 18]})
  df2 = pd.DataFrame({"id": [5, 3], "des": ['帅哥', '帅锅']})
  df3 = pd.DataFrame({"id": [4], "name": ['nmm'], "age": [16]})
  print(merge_data(df1, df2))
  print(concat_data(df1, df3))
  print(delete_row_data(df1))
  print(delete_col_data(df1))
