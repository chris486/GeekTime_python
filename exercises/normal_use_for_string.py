name = 'derek'
print(name.capitalize())            #首字母大写  Derek
print(name.count("e"))              #统计字符串出现某个字符的个数
print(name.center(10,'*'))          #打印10个字符，不够的“*”补齐
print(name.endswith('k'))           #判断字符串是否以"k"结尾
print('244'.isdigit())              #判断字符是否为整数
print('+'.join(['1','2','3']))      #把join后的内容加入到前面字符串中，以+为分割符
print('\n123'.strip())              #strip去掉换行符
print("1+2+3+4".split("+"))         #以+为分隔符生成新的列表，默认不写为空格

msg = 'my name is {name} and i am {age} old'
print(msg.format(name='Tom',age=20))
