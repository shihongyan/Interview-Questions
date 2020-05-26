import pandas as pd
import numpy as np
import pylab as pl
from sklearn import linear_model
from sklearn import cross_validation
#from sklearn import linear_model
#导入交叉验证库
#from sklearn import cross_validation
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

#输入文件的地址
excelFile = 'C:\\Users\\FuturePlayer\\Desktop\\protest\\protest\\test3\\cc.xlsx'
#读取数据转化为dataframe-----总共有4028行记录，10列字段------sheet1中的数据
df = pd.DataFrame(pd.read_excel(excelFile))
#对样本中的各变量进行描述性分析
print(df.describe())
#对样本进行交叉频数分析 对比流失用户与每个因素的关系
print(pd.crosstab(df['流失用户'],df['套餐金额'],rownames=['流失用户']))
print(pd.crosstab(df['流失用户'],df['额外通话时长'],rownames=['流失用户']))
print(pd.crosstab(df['流失用户'],df['额外流量'],rownames=['流失用户']))
print(pd.crosstab(df['流失用户'],df['改变行为'],rownames=['流失用户']))
print(pd.crosstab(df['流失用户'],df['服务合约'],rownames=['流失用户']))
print(pd.crosstab(df['流失用户'],df['关联购买'],rownames=['流失用户']))
print(pd.crosstab(df['流失用户'],df['集团用户'],rownames=['流失用户']))
print(pd.crosstab(df['流失用户'],df['使用月数'],rownames=['流失用户']))
#准备要拟合的数据
df_1=pd.get_dummies(df['套餐金额'],prefix='套餐金额')
print(df_1.head())
df_2=pd.get_dummies(df['额外通话时长'],prefix='额外通话时长')
print(df_2.head())
df_3=pd.get_dummies(df['额外流量'],prefix='额外流量')
print(df_3.head())
df_4=pd.get_dummies(df['改变行为'],prefix='改变行为')
print(df_4.head())
df_5=pd.get_dummies(df['服务合约'],prefix='服务合约')
print(df_5.head())
df_6=pd.get_dummies(df['关联购买'],prefix='关联购买')
print(df_6)
df_7=pd.get_dummies(df['集团用户'],prefix='集团用户')
print(df_7.head())
df_8=pd.get_dummies(df['使用月数'],prefix='使用月数')
print(df_8.head())
#手动进行数据拼接 ----拟合Logit模型
df_a=['流失用户','额外通话时长','额外流量','使用月数']
data=df[df_a].join(df_1.iloc[0:4028,1:3]).join(df_4.iloc[0:4028,1:2])\
    .join(df_5.iloc[0:4028,1:2]).join(df_6.iloc[0:4028,1:3]).join(df_7.iloc[0:4028,1:2])
print(data)
data['intercept']=1.0
trains_col=data.columns[1:]
logit = sm.Logit(data['流失用户'],data[trains_col])
result=logit.fit()
print(result.summary())
print(result)
#套餐金额_2 + 套餐金额_3 + 改变行为_1+服务合约_1+关联购买_1+关联购买_2+集团用户_1+使用月数
formula = '流失用户~ 套餐金额+额外通话时长+额外流量+ 改变行为+服务合约+关联购买+集团用户+使用月数 '
anova_results = anova_lm(ols(formula,df).fit())
print(anova_results)
print(pairwise_tukeyhsd(df['流失用户'], df['套餐金额']))
#-----------------------------------------准备数据获取前111行记录-----------------------------------------#
mydata=df.iloc[0:112,1:10]
print(mydata)
#对数据进行训练和预测  以'套餐金额为例'
#将广告成本设为自变量X,'改变行为','服务合约','关联购买','集团用户'套餐金额
X = np.array(mydata[['套餐金额']])
#将点击量设为因变量Ya
Y = np.array(mydata['流失用户'])
#查看自变量和因变量的行数
print(X.shape,Y.shape)
#绘制散点图
plt.scatter(X,Y,60,color='blue',marker='o',linewidth=3,alpha=0.8)
#显示图表
plt.show()
#切分训练集和测试集
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.4, random_state=0)
print(X_train.shape,y_train.shape)
clf = linear_model.LinearRegression()
clf.fit (X_train,y_train)
list(clf.predict(X_test))
#显示测试集的因变量
list(y_test)
#计算误差平方和
last=((y_test - clf.predict(X_test)) **2).sum()
print(last)



