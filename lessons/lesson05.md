# 字符串 

### 字符串的基础

字符串：由独立字符组成的一个序列，通常包含在单引号（' '）双引号（" "）或者三引号之中（''' '''或""" """，两者一样）

```
eg.
s1 = 'hello'
s2 = "hello"
s3 = """hello"""
s1 == s2 == s3
True
```

### 字符串的常用操作

Python 的字符串是不可变的（immutable）

```
s = 'hello'
s[0] = 'H'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

> 自从 Python2.5 开始，每次处理字符串的拼接操作时 `（str1 += str2）`，Python 首先会检测 str1 还有没有其他的引用。如果没有的话，就会尝试原地扩充字符串 buffer 的大小，而不是重新分配一块内存来创建新的字符串并拷贝。这样的话，`（str1 += str2）`的时间复杂度就仅为 O(n) 了。

```
l = []
for n in range(0, 100000):
    l.append(str(n))
l = ' '.join(l)

```

> 由于列表的 append 操作是 O(1) 复杂度，字符串同理。因此，这个含有 for 循环例子的时间复杂度为 n*O(1)=O(n)。



### 格式化字符串

`print('no data available for person with id: {}, name: {}'.format(id, name))`

`print('no data available for person with id: %s, name: %s' % (id, name))`

**3.7 之后的 python 提倡使用 `f-string` 字面量格式化字符串**
```
a, b = 'hello', 'world' 
print(f'{a} {b}')
```

**更多字符串连接方式见python3基础笔记**