#数据类型：列表，元组，字典，集合
#列表
lists = ['a','b','c']
print(lists)
print(len(lists))
lists.append('d')
print(lists)
lists.pop()
print(lists)
lists.insert(0,'2')
print(lists)

#元组
tuple = ('tupleA','tupleB')
print(tuple[0])

#字典
name={'a':89,'b':90}
name['c']=99
print(name)
name.pop('c')
print(name)
print ('aa' in name)
print(name.get('a'))
print(name.get('a1',88))

#集合
s = set(['a','b','c'])
s.add('d')
s.remove('b')
print(s)
print('qq' in s)