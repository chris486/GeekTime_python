from timeit import timeit

# 测试元组与列表所占用存储的区别
tu = (1,2,3,4,5,6,7,8,9,10)
print(tu.__sizeof__())

li = [1,2,3,4,5,6,7,8,9,10]
print(li.__sizeof__())

# 测试创建元组与列表所需时间
t1 =timeit('x=(1,2,3,4,5,6)',number=1000000)
print(t1)
t2 = timeit('x=[1,2,3,4,5,6,]',number=1000000)
print(t2)

# 测试不同方法创建列表所需时间
t11 = timeit('empty_list = list()')
print(t11)
t22 = timeit('empty_list = []')
print(t22)


