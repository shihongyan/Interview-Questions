#建立df存储数据平均值，方差等数据
df_num = pd.DataFrame(columns = ['最小值','1/4位数','中位数','3/4位数','最大值'])
list1=np.array(df.iloc[1:4029,1:2]).tolist()
list_num1=list(chain.from_iterable(list1))
list2=np.array(df.iloc[1:4029,2:3]).tolist()
list_num2=list(chain.from_iterable(list2))
list3=np.array(df.iloc[1:4029,3:4]).tolist()
list_num3=list(chain.from_iterable(list3))
list4=np.array(df.iloc[1:4029,4:5]).tolist()
list_num4=list(chain.from_iterable(list4))
list5=np.array(df.iloc[1:4029,5:6]).tolist()
list_num5=list(chain.from_iterable(list5))
list6=np.array(df.iloc[1:4029,6:7]).tolist()
list_num6=list(chain.from_iterable(list6))
list7=np.array(df.iloc[1:4029,7:8]).tolist()
list_num7=list(chain.from_iterable(list7))
list8=np.array(df.iloc[1:4029,8:9]).tolist()
list_num8=list(chain.from_iterable(list8))
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
data_dict5 = {
    '最小值':min(list_num5),
    '中位数': median(list_num5),
    '最大值':max(list_num5),
}
data_dict6 = {
    '最小值':min(list_num6),
    '中位数': median(list_num6),
    '最大值':max(list_num6),
}
data_dict7 = {
    '最小值':min(list_num7),
    '中位数': median(list_num7),
    '最大值':max(list_num7),
}
data_dict8 = {
    '最小值':min(list_num8),
    '中位数': median(list_num8),
    '最大值':max(list_num8),
}
df_num=pd.DataFrame(data=data_dict1,index = [0]).append(pd.DataFrame(data=data_dict2,index = [0]))\
    .append(pd.DataFrame(data=data_dict3,index = [0])).append(pd.DataFrame(data=data_dict4,index = [0]))\
    .append(pd.DataFrame(data=data_dict5,index = [0]))\
    .append(pd.DataFrame(data=data_dict6,index = [0]))\
    .append(pd.DataFrame(data=data_dict7,index = [0]))\
    .append(pd.DataFrame(data=data_dict8,index = [0]))
print("原始数据df中数量统计值如下：")
print(df_num)
print("df中1/4分位数：")
print(df.quantile(.25))
print("df中3/4分位数：")
print(df.quantile(.75))



