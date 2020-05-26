import pandas as pd
import scipy.stats as stats
import numpy as np
from itertools import chain
#from sklearn import linear_model
from numpy import mean, median, var, std
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy.stats import ttest_ind,norm,f
import matplotlib.pyplot as plt
import math

#输入文件的地址
csvFile = 'C:\\Users\\FuturePlayer\\Desktop\\protest\\protest\\test2\\bb.csv'
#-----------------------------------------------准备数据------------------------------------#
#读取数据转化为dataframe
df = pd.DataFrame(pd.read_csv(csvFile))
#第一种数据---------------截取r1,r2,r3,r4列的数据，赋值给y
y=df.iloc[0:100,0:4]
print(y)
#第二种数据---------------mydata
a1=df.iloc[0:100,0:1].rename(columns={'r1':'y'})
a1.insert(0,'x','1')
a2=df.iloc[0:100,1:2].rename(columns={'r2':'y'})
a2.insert(0,'x','2')
a3=df.iloc[0:100,2:3].rename(columns={'r3':'y'})
a3.insert(0,'x','3')
a4=df.iloc[0:100,3:4].rename(columns={'r4':'y'})
a4.insert(0,'x','4')
mydata=a1.append(a2).append(a3).append(a4)
print(mydata)

#-----------------------------------------------数据分析------------------------------------#
###############判断y是否符合正态分布
print("y中数据是否符合正态分布：")
print(stats.shapiro(y))

################方差分析计算
formula = 'y~C(x)'
anova_results = anova_lm(ols(formula,mydata).fit())
print("方差分析计算：")
print(anova_results)

#############显示y中每一列的最小值，1/4位数，中位数，均值，3/4位数
#建立df存储数据平均值，方差等数据
df_num = pd.DataFrame(columns = ['最小值','1/4位数','中位数','3/4位数','最大值'])
list1=np.array(df.iloc[0:100,0:1]).tolist()
list_num1=list(chain.from_iterable(list1))
list2=np.array(df.iloc[0:100,1:2]).tolist()
list_num2=list(chain.from_iterable(list2))
list3=np.array(df.iloc[0:100,2:3]).tolist()
list_num3=list(chain.from_iterable(list3))
list4=np.array(df.iloc[0:100,3:4]).tolist()
list_num4=list(chain.from_iterable(list4))
data_dict1 = {
    '最小值':min(list_num1),
    '中位数': median(list_num1),
    '最大值':max(list_num1),
}
data_dict2 = {
    '最小值':min(list_num2),
    '中位数': median(list_num2),
    '最大值':max(list_num2),
}
data_dict3 = {
    '最小值':min(list_num3),
    '中位数': median(list_num3),
    '最大值':max(list_num3),
}
data_dict4 = {
    '最小值':min(list_num4),
    '中位数': median(list_num4),
    '最大值':max(list_num4),
}
df_num=pd.DataFrame(data=data_dict1,index = [0]).append(pd.DataFrame(data=data_dict2,index = [0]))\
    .append(pd.DataFrame(data=data_dict3,index = [0])).append(pd.DataFrame(data=data_dict4,index = [0]))
print("y中数量统计值如下：")
print(df_num)
print("y中1/4分位数：")
print(y.quantile(.1))
print("y中3/4分位数：")
print(y.quantile(.3))

##########################  t检验  α=0.05
print(stats.ttest_1samp(y['r1'],0.9))
print(stats.ttest_1samp(y['r2'],0.9))
print(stats.ttest_1samp(y['r3'],0.9))
print(stats.ttest_1samp(y['r4'],0.9))

#-----------------------------------------------准备数据-----------------------------------#
b1=df[['r2','s2']].rename(columns={'r2':'x','s2':'y'})
b2=df[['r4','s4']].rename(columns={'r4':'x','s4':'y'})
mydata1=b1.append(b2)
print(mydata1)

#----------------------------------------------相关性系数计算-----------------------------#
print('X,Y的相关系数：')
print(mydata1.corr())
#-----------------------------------------------线性回归统计-----------------------------#
#model = linear_model.LinearRegression()
#model.fit(mydata1['x'],mydata1['y'])
#-------------------------------------某一函数的计算并绘制图表-----------------------------#
df_ab = pd.DataFrame(columns = ['a','b'])
for i in range(0,201):
    temp_ab=0.00007661*i*i-0.01814*i+0.98
    df_ab.loc[i] = [i, temp_ab]
plt.bar(df_ab['a'], df_ab['b'])
plt.show()

#-------------------------------------开始求范围-------------------------------------#
#d = symbols('d')
#solve(Eq(d**2*0.00007661+0.01814*d+0.98),x)
#----求在50-100之间的根
args=[0.00007661,-0.01814,0.98]
for j in (0,np.roots(args).size-1):
    if np.roots(args)[j]>50 :
        if np.roots(args)[j]<100 :
            d=np.roots(args)[j]
print(d)
#----求出平方差
e=std(df_ab['b'])
print(df_ab['b'])
print(e)
min=d-df_ab['a'].quantile(.025)*e/math.sqrt(199)
max=d+df_ab['a'].quantile(.025)*e/math.sqrt(199)
print(min,max)