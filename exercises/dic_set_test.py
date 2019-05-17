# 字典
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
d1 == d2 == d3 ==d4

# 集合
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
s1 == s2

# get 函数索引
d = {'name': 'jason', 'age': 20}
d.get('name')
d.get('location')
d.get('location' , 'null')

# 判断值是否在 dic 或 set 内

d = {'name': 'jason', 'age': 20}
'name' in d
'location' in d
'jason' in d