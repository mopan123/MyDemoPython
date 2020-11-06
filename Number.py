# @Time    : 2020/9/16 11:45
# @Author  : mopan
# @File    : Number.py
# @Software: PyCharm

f1 = 12.5
print("f1Value: ", f1)
print("f1Type: ", type(f1))

f2 = 0.34557808421257003
print("f2Value: ", f2)
print("f2Type: ", type(f2))

f3 = 0.0000000000000000000000000847
print("f3Value: ", f3)
print("f3Type: ", type(f3))

f4 = 345679745132456787324523453.45006
print("f4Value: ", f4)
print("f4Type: ", type(f4))

f5 = 12e4
print("f5Value: ", f5)
print("f5Type: ", type(f5))

f6 = 12.3 * 0.1
print("f6Value: ", f6)
print("f6Type: ", type(f6))


c1 = 12 + 0.2j
print("c1Value: ", c1)
print("c1Type", type(c1))

c2 = 6 - 1.2j
print("c2Value: ", c2)

#对复数进行简单计算
print("c1+c2: ", c1+c2)
print("c1*c2: ", c1*c2)

str = "I\"love python"
str1 = 'I\'love python'

str1 = "I'm a great coder!"  #使用双引号包围含有单引号的字符串
str2 = '引文双引号是"，中文双引号是“'  #使用单引号包围含有双引号的字符串
print(str)
print(str1)

s2 = 'It took me six months to write this Python tutorial. \
    Please give me more support. \
    I will keep it updated.'

print(s2)

num = 20 + 3 / 4 + \
    2 * 3
print(num)

str1 = r'I\'m a great coder!'
print(str1)

rstr = r'D:\Program Files\Python 3.8\python.exe'
print(rstr)
str1 = r'D:\Program Files\Python 3.8' '\\'  #D:\Program Files\Python 3.8\
print(str1)

#通过构造函数创建空bytes

b1 = bytes()

#通过空字符串创建空 bytes

b2 = b''

#通过b前缀将字符串转换成 bytes
b3 = b'http://c.biancheng.net/python/'
print("b3: ", b3)
print(b3[3])
print(b3[7:22])

#为 bytes() 方法指定字符集
b4 = bytes('C语言中文网8岁了',encoding='UTF-8')
print("b4: ", b4)
#通过 encode() 方法将字符串转换成 bytes
b5 = "C语言中文网8岁了".encode('UTF-8')
print("b5: ", b5)

#通过 decode() 方法将 bytes 转换成字符串
str1 = b5.decode('UTF-8')
print("str1: ", str1)


a = input("Enter a number: ")
b = input("Enter another number: ")

a = float(a)

b = float(b)

print("aType: ", type(a))
print("bType: ", type(b))

result = a + b
print("resultValue: ", result)
print("resultType: ", type(result))
