# @Time    : 2020/10/14 10:25
# @Author  : mopan
# @File    : PySenior.py
# @Software: PyCharm

user = 'mopan'
user_age =24
#同时输出多个变量和字符串
print("姓名：",user,'年龄：',user_age)
print("姓名：",user,'年龄：',user_age, sep='|')

print(10,'\t',end='')
"或者这么写 print(10,,end='\t')"
print(20,'\t',end='')
print(30,'\t',end='')

f = open("demo.txt","w")#打开文件以便写入
print('沧海月明珠有泪',file=f)
print('蓝回日暖玉生烟',file=f)
f.close()



"双引号 多行注释"
'''三个单引号 也是多行注释'''