# @Time    : 2020/11/6 15:06
# @Author  : mopan
# @File    : 字符串常用的方法.py
# @Software: PyCharm

a = '123134'
print(len(a))
"""
在 Python 中，不同的字符所占的字节数不同，数字、英文字母、小数点、下划线以及空格，各占一个字节，而一个汉字可能占 2~4 个字节，
具体占多少个，取决于采用的编码方式。例如，汉字在 GBK/GB2312 编码中占用 2 个字节，而在 UTF-8 编码中一般占用 3 个字节。
>>> str1 = "人生苦短，我用Python"
>>> len(str1.encode())
27
因为汉字加中文标点符号共 7 个，占 21 个字节，而英文字母和英文的标点符号占 6 个字节，一共占用 27 个字节。
同理，如果要获取采用 GBK 编码的字符串的长度，可以执行如下代码：
>>> str1 = "人生苦短，我用Python"
>>> len(str1.encode('gbk'))
20
"""

'''
split() 方法可以实现将一个字符串按照指定的分隔符切分成多个子串，
这些子串会被保存到列表中（不包含分隔符），作为方法的返回值反馈回来。该方法的基本语法格式如下：
str.split(sep,maxsplit)
str：表示要进行分割的字符串；
sep：用于指定分隔符，可以包含多个字符。此参数默认为 None，表示所有空字符，包括空格、换行符“\n”、制表符“\t”等。
maxsplit：可选参数，用于指定分割的次数，最后列表中子串的个数最多为 maxsplit+1。如果不指定或者指定为 -1，则表示分割次数没有限制。
'''

str = "fwtwtwt,2424,trhh"
print(str.split())
print(str.split(','))
print(str.split('2',2))
#需要注意的是，在未指定 sep 参数时，split() 方法默认采用空字符进行分割，
# 但当字符串中有连续的空格或其他空字符时，都会被视为一个分隔符对字符串进行分割，例如：
str = "sfet,  ,rer,wrw"
print(str.split())

"""
join() 方法也是非常重要的字符串方法，它是 split() 方法的逆方法，用来将列表（或元组）中包含的多个字符串连接成一个字符串。
join() 方法的语法格式如下：
newstr = str.join(iterable)
此方法中各参数的含义如下：
newstr：表示合并后生成的新字符串；
str：用于指定合并时的分隔符；
iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供。
"""
list =["asf","fsf","ww"]
print("/".join(list))
yuanzu =("","d","f")
print("-".join(yuanzu))

"""
count 方法用于检索指定字符串在另一字符串中出现的次数，如果检索的字符串不存在，则返回 0，否则返回出现的次数。
count 方法的语法格式如下：
str.count(sub[,start[,end]])
此方法中，各参数的具体含义如下：
str：表示原字符串；
sub：表示要检索的字符串；
start：指定检索的起始位置，也就是从什么位置开始检测。如果不指定，默认从头开始检索；
end：指定检索的终止位置，如果不指定，则表示一直检索到结尾。
"""
jiancha = "s.fdfdfs.ggg"
print(jiancha.count('f',3,-6))

"""
find() 方法用于检索字符串中是否包含目标字符串，如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。
find() 方法的语法格式如下：
str.find(sub[,start[,end]])
此格式中各参数的含义如下：
str：表示原字符串；
sub：表示要检索的目标字符串；
start：表示开始检索的起始位置。如果不指定，则默认从头开始检索；
end：表示结束检索的结束位置。如果不指定，则默认一直检索到结尾。
"""
jiancha = "s.fdfdfs.ggg"
print(jiancha.find('f',3,-6))

"""
同 find() 方法类似，index() 方法也可以用于检索是否包含指定的字符串，不同之处在于，当指定的字符串不存在时，index() 方法会抛出异常。
同 find() 和 rfind() 一样，字符串变量还具有 rindex() 方法，其作用和 index() 方法类似，不同之处在于它是从右边开始检索，例如：
>>> str = "c.biancheng.net"
>>> str.rindex('.')
11
"""
