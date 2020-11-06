# @Time    : 2020/11/5 10:04
# @Author  : mopan
# @File    : Gsh.py
# @Software: PyCharm

# name = '我爱Python'
# age = 15
# print("%s已经%d岁" % (name,age))
#
# n = 1234567
# print("n(10):%10d." % n)
# print("n(5):%5d." % n)
#
# url = "http://c.biancheng.net/python/"
# print("url(35):%35s." % url)
# print("url(20):%20s." % url)

'''
对于整数，指定左对齐时，在右边补 0 是没有效果的，因为这样会改变整数的值。
对于小数，以上三个标志可以同时存在。
对于字符串，只能使用-标志，因为符号对于字符串没有意义，而补 0 会改变字符串的值。
'''

n = 123456
# %09d 表示最小宽度为9，左边补0
print("n(09):%09d" % n)
# %+9d 表示最小宽度为9，带上符号
print("n(+9):%+9d" % n)

f = 140.5
# %-+010f 表示最小宽度为10，左对齐，带上符号
print("f(-+0):%-+010f" % f)

s = "Hello"
# %-10s 表示最小宽度为10，左对齐
print("s(-10):%-10s." % s)

"""
%m.nf
%.nf
m 表示最小宽度，n 表示输出精度，.是必须存在的。
"""

f =3.141592653
# 最小宽度为8，小数点后保留3位
print('%8.3f'%f)
# 最小宽度为8，小数点后保留3位，左边补0
print("%08.3f"%f)
# 最小宽度为8，小数点后保留3位，左边补0，带符号
print("%+08.3f"%f)

print("转义字符串分割线————————————————")
str1 = "Oct: \061\062\063"
str2 = "Hex: \x31\x32\x33\x78\x79\x7A"
print(str1)
print(str2)


#使用\t排版
str1 = '网站\t\t域名\t\t\t年龄\t\t价值'
str2 = 'C语言中文网\tc.biancheng.net\t\t8\t\t500W'
str3 = '百度\t\twww.baidu.com\t\t20\t\t500000W'
print(str1)
print(str2)
print(str3)
print("--------------------")
# \n在输出时换行，\在书写字符串时换行
info = "Python教程：http://c.biancheng.net/python/\n\
C++教程：http://c.biancheng.net/cplus/\n\
Linux教程：http://c.biancheng.net/linux_tutorial/"
print(info)

print("\"qwe\"")


url = "http://c.biancheng.net/cplus/"

# print("----False and xxx-----")
# print( False and print(url) )
print("----True and xxx-----")
print( True and print(url) )
# print("----False or xxx-----")
# print( False or print(url) )
# print("----True or xxx-----")
# print( True or print(url) )

'''
使用 if else 实现三目运算符
exp1 if contion else exp2
condition 是判断条件，exp1 和 exp2 是两个表达式。如果 condition 成立（结果为真），
就执行 exp1，并把 exp1 的结果作为整个表达式的结果；如果 condition 不成立（结果为假），
就执行 exp2，并把 exp2 的结果作为整个表达式的结果。
'''
aa = 5;
bb = 6;
cc = 7;
max = aa if aa > bb else (  cc if cc < bb else bb)
print(max)

"""
sname[start : end : step]
sname：表示序列的名称；
start：表示切片的开始索引位置（包括该位置），此参数也可以不指定，会默认为 0，也就是从序列的开头进行切片；
end：表示切片的结束索引位置（不包括该位置），如果不指定，则默认为序列的长度；
step：表示在切片过程中，隔几个存储位置（包含当前位置）取一次元素，也就是说，如果 step 的值大于 1，
则在进行切片去序列元素时，会“跳跃式”的取元素。如果省略设置 step 的值，则最后一个冒号就可以省略。
"""

str="C语言中文网"
#取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
print(str[:2])
#隔 1 个字符取一个字符，区间是整个字符串
print(str[1::2])
#取整个字符串，此时 [] 中只需一个冒号即可
print(str[:])

"""
value in sequence
value 表示要检查的元素，sequence 表示指定的序列
"""
str="c.biancheng.net"
print("c" in str)

#内置函数
# print(max(str))
print(min(str))
print(sorted(str))