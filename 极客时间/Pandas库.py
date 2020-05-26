import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import xlrd

#Series有两个基本属性，index和values，index默认的是0，1，2递增整数序列，也可以自己定义索引
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4],index=['a','b','c','d'])
print(x1)
print(x2)

d = {'a':1,'b':2,'c':3}
x = Series(d)
print(x)

#DataFrame
data = {'chinese':[66, 95, 93, 90,80],'数学':[30, 98, 96, 77, 90],'英语':[65, 85, 92, 88, 90]}
#默认0-n数字索引
df = DataFrame(data)
#指定索引类型
df1 = DataFrame(data,index=['张飞','赵云','李白','亚瑟','韩信'],columns=['语文','数学','英语'])
print(df)
print(df1)

df2 = DataFrame(pd.read_excel('C:\\Users\\lishikang\\Desktop\\数据分析\\极客时间-数据分析\\pandas库.xlsx'))
print(df2)
#将dataframe写入表格中
#df2.to_excel('url')

#删除字段-某一列  将新的表赋值给另一个dataframe
df3 = df.drop(columns=['chinese'])
print(df3)

#将字段名重新命名
df.rename(columns={'chinese':'语文','英语':'English'},inplace=True)
print(df)

#去除重复的行  并将其赋值给新的的dataframe
df22=df2.drop_duplicates()

#格式问题：更改数据格式
df22['语文'].astype('str')
#df22['语文'].astype(np.int64)

#数据间的空格
#删除两边
df22['语文']=df22['语文'].map(str.strip)
#删除特殊字符
df22['语文']=df22['语文'].str.strip('%')
#删除左边空格
df22['语文']=df22['语文'].map(str.lstrip)
#删除右边空格
df22['语文']=df22['语文'].map(str.rstrip)
print(df22)

#全部大写
df22.columns=df22.columns.str.upper()
#全部小写
df22.columns=df22.columns.str.lower()
#首字母大写
df22.columns=df22.columns.str.title()

df22.isnull()



