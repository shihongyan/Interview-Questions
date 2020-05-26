import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain
from numpy import mean, median, var, std
import seaborn as sns
from scipy import stats
from itertools import groupby
#输入文件的地址
excelFile = 'C:\\Users\\FuturePlayer\\Desktop\\protest\\protest\\test1\\aa.xlsx'
#读取数据转化为dataframe
df = pd.DataFrame(pd.read_excel(excelFile))
#-------------------------准备数据------------------------#
#计算每一行的数值
df['Col_sum'] = df.loc[0:12, ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']].apply(lambda x: x.sum(), axis=1)
#计算每一列的数值
df.loc['Row_sum'] = df.apply(lambda x: x.sum())
#获取每行的总数列
df1=df['Col_sum'][0:12]
#获取每一列的总数行
df2=df.iloc[12,1:13]
#获取表中年份
year=df.iloc[0:12,0]
#获取表中月份
month=list(df)
del month[0]
del month[12]
#-----------------------绘制图表-------------------------#
#绘制barplot图，以年份为横轴
plt.bar(year, df1)
plt.show()
#绘制折线图
plt.plot(year, df1, linewidth=5, color='y')
plt.show()
#绘制barplot图，以月份为横轴
plt.bar(month, df2,color='r')
plt.show()
#----------------------数据分析-------------------------#
#转换数据存储格式，准备分析的数据
list1=np.array(df.iloc[0:12,1:13]).tolist()
list_num=list(chain.from_iterable(list1))
#建立df存储数据平均值，方差等数据
df_num = pd.DataFrame(columns = ['平均数','标准差','方差','中位数','最小值','最大值','偏度','峰度'])
#描述性分析数据的统计量
data_dict = {
    '平均数':mean(list_num),
    '标准差':std(list_num),
    '方差':var(list_num),
    '中位数':median(list_num),
    '最小值':min(list_num),
    '最大值':max(list_num),
    '偏度':stats.skew(list_num),
    '峰度':stats.kurtosis(list_num)
}
df_num=pd.DataFrame(data=data_dict,index = [0])
#---------显示以上字段的数据
print(df_num)
#-----------绘制频数直方图
plt.hist(list_num)
plt.show()
#----------拟合画线
sns.distplot(list_num,color="r",bins=50,kde=True)
plt.show()
#------绘制茎叶图
for k, g in groupby(sorted(list_num), key=lambda x: int(x) // 10):
    #print('k', k)
    #print('g', list(g))
    lst = map(str, [int(y) % 10 for y in list(g)])
    print (k, '|', ' '.join(lst))
#------绘制箱线图
df_x=df.iloc[0:12,1:13]
print(df_x.transpose())
plt.boxplot(df_x)
plt.show()
#绘制QQ图
stats.probplot(list_num, dist="norm", plot=plt)
plt.show()


