# 输入和输出

## 基本的输入输出

input() 函数暂停程序运行，同时等待键盘输入，直到回车被按下。

函数的参数即为提示语，输入的类型永远是字符串型（str）

## 文件的输入输出

open() 函数对应于 close() 函数，也就是说，如果你打开了文件，在完成读取任务后，就应该立刻关掉它。

在 with 的语境下任务执行完毕后，close() 函数会被自动调用，就不需要显式调用 close()，代码也简洁很多。

## json 序列化

json.dumps() 这个函数，接受 Python 的基本数据类型，然后将其序列化为 string；

**json.dumps() : dict --> str**

json.loads() 这个函数，接受一个合法字符串，然后将其反序列化为 Python 的基本数据类型。

**json.loads()： str --> dict**