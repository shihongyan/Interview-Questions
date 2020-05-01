import numpy as np
#dtype定义数据类型，name字段名称，formats表示字段的数据类型in,
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(persontype)
print(peoples)
print (np.mean(ages))
print (np.mean(chineses))
print (np.mean(maths))
print (np.mean(englishs))