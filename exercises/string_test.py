# 注意查看代码执行时间
s = ''
for n in range(0, 100):
    s += str(n)

print(s)

# 注意查看代码执行时间
l = []
for n in range(0, 100000):
    l.append(str(n))
    
s = ' '.join(l)
print(s)

