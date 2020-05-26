import numpy as np
import pandas as pd
#------------结果数组-------------------#
#dtype定义数据类型，name字段名称，formats表示字段的数据类型in,
# persontype = np.dtype({
#     'names':['name', 'age', 'chinese', 'math', 'english'],
#     'formats':['S32','i', 'i', 'i', 'f']})
# peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
#        ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
#     dtype=persontype)
# ages = peoples[:]['age']
# chineses = peoples[:]['chinese']
# maths = peoples[:]['math']
# englishs = peoples[:]['english']
# print(persontype)
# print(peoples)
# print (np.mean(ages))
# print (np.mean(chineses))
# print (np.mean(maths))
# print (np.mean(englishs))

#----连续数组的创建-----#

#初始值，终值，步长
x1=np.arange(1,11,2)
#初始值，终值，元素个数
x2=np.linspace(1,9,5)
print(np.add(x1,x2))
print(np.subtract(x1,x2))
print(np.multiply(x1,x2))
print(np.divide(x1,x2))
print(np.power(x1,x2))
#取余函数 remainder()=mod()
print(np.remainder(x1,x2))
print(np.mod(x1,x2))

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.amin(a))
#一行中的最小值,分组[1，4，7],[2,5,8],[3,6,9]
print(np.amin(a,0))
#一列中的最小值[1,2,3][4,5,6][7,8,9]
print(np.amin(a,1))
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))

#统计最大值与最小值之差ptp()
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))

#统计数组的百分位数percentile()
#代表着第P个百分位数，这里P的取值范围是0-100，如果p=0,那么求最小值，50=平均值，100=最大值
print(np.percentile(a,50))
#求得每一列的平均值
print(np.percentile(a,50,axis=0))
#求每一行的平均值
print(np.percentile(a,50,axis=1))

#同理：中位数：median(),平均数mean()

#求中位数
print(np.median(a))
print(np.median(a,axis=0))
print(np.median(a,axis=1))

#求平均值
print(np.mean(a))
print(np.mean(a,axis=0))
print(np.mean(a,axis=1))

#统计数组中的加权平均值average()
b=np.array([1,2,3,4])
wts=np.array([1,2,3,4])
print(np.average(b))
print(np.average(b,weights=wts))

#标准差std()和方差var()
print(np.std(b))
print(np.var(b))

#NumPy排序
#sort(a,axis=-1,kind='quicksort',order=None) 默认情况下使用的是快速排序，kind中可以指定quicksort,mergesort,heapsort分别表示快速排序，合并排序，堆排序
#axis默认的是-1，可以取不同的axis轴，axis=None代表采用扁平化的方式作为一个向量进行排序，order字段，对于结构化的数组可以指定按照某一个字段进行排序
a=np.array([[4,3,2],[2,4,1]])
#对数组中的每一个元素内的数值进行排序
print(np.sort(a))
#对所有数字进行排序
print(np.sort(a,axis=None))
#对列进行排序
print(np.sort(a,axis=0))
#对行进行排序
print(np.sort(a,axis=1))

#作业
#定义结构数组的类型     formats中的S32不支持中文，用U32
gradetype = np.dtype({
    'names':['name','语文','英语','数学'],
    'formats':['U32','i', 'i', 'i']})
grade = np.array([("张飞",66,65,30),
                  ("关羽",95,85,98),
                  ("赵云",93,92,96),
                  ("huangzhong",90,88,77),
                  ("dianwei",80,90,90)],dtype=gradetype)
#grade =grade.encode('ascii').decode('unicode_escape')
yuwen=grade[:]['语文']
shuxue=grade[:]['数学']
yingyu=grade[:]['英语']

#
# #平均成绩
# print('-----各科平均值-----')
# print(np.mean(yuwen))
# print(np.mean(shuxue))
# print(np.mean(yingyu))
#
# #最小成绩
# print('-----各科最小值-----')
# print(np.amin(yuwen))
# print(np.amin(shuxue))
# print(np.amin(yingyu))
#
# #最大成绩
# print('-----各科最大值-----')
# print(np.amax(yuwen))
# print(np.amax(shuxue))
# print(np.amax(yingyu))
#
# #方差
# print('-----方差-----')
# print(np.var(yuwen))
# print(np.var(shuxue))
# print(np.var(yingyu))
#
# print('-----标准差-----')
# print(np.std(yuwen))
# print(np.std(shuxue))
# print(np.std(yingyu))

def show(name,cj):
    print('{}|{}|{}|{}|{}|{}'.format(name,np.mean(cj),np.min(cj),np.max(cj),np.var(cj),np.std(cj)))

print("科目|平均分|方差|标准差|最低分|最高分")
show("数学",shuxue)
show("语文",yuwen)
show("英语",yingyu)

print("排名")
ranking = sorted(grade,key=lambda x:x[1]+x[2]+x[3],reverse=True)
print(ranking)