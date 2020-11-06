# @Time    : 2020/11/5 17:45
# @Author  : mopan
# @File    : 列表元素字典集合.py
# @Software: PyCharm

"""
Python创建列表
1) 使用 [ ] 直接创建列表
2) 使用 list() 函数创建列表
"""
num = [1, 2, 3, 4, 5, 6, 7]
name = ["C语言中文网", "http://c.biancheng.net"]
program = ["C语言", "Python", "Java"]
empytlist =[]

#将字符串转换成列表
list1 = list("hello")
print(list1)

#将元组转换成列表
tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
list2 = list(tuple1)
print(list2)

#将字典转换成列表
dict1 = {'a':100, 'b':42, 'c':9}
list3 = list(dict1)
print(list3)

#将区间转换成列表
range1 = range(1, 6)
list4 = list(range1)
print(list4)

#创建空列表
print(list())

"""
访问列表元素
"""

url = list("http://c.biancheng.net/shell/")
# 使用索引访问列表元素的格式为：listname[i] 其中，listname 表示列表名字，i 表示索引值。列表的索引可以是正数，也可以是负数。
print(url[3])
print(url[-5])
#使用切片访问列表元素的格式为：listname[start : end : step] listname 表示列表名字，start 表示起始索引，end 表示结束索引，step 表示步长。
print(url[3:5:])
print(url[:5:2])
print(url[-5:-1])
#del url
#print(url)

#添加元素
liebiao = ["a","b","c"]
liebiao.append("d")
print(liebiao)

liebiao.extend("f")
print(liebiao)

liebiao.insert(2,"gg")

lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
lang.clear()
del lang[1: 4]
# lang.pop()
print(lang)

"""
Python list列表查找元素

listname.index(obj, start, end)
listname 表示列表名称，obj 表示要查找的元素，start 表示起始位置，end 表示结束位置。
"""
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
#检索列表中的所有元素
print( nums.index(2) )
#检索3~7之间的元素
print( nums.index(100, 3, 7) )
#检索4之后的元素
print( nums.index(7, 4) )
#检索一个不存在的元素
# print( nums.index(55) )

print("%d次" % nums.count(36))

"""
元组(tuple)和列表（list）的不同之处在于：
列表的元素是可以更改的，包括修改元素值，删除和插入元素，所以列表是可变序列；
而元组一旦被创建，它的元素就不可更改了，所以元组是不可变序列。
在 Python 中，元组通常都是使用一对小括号将所有元素包围起来的，但小括号不是必须的，只要将各元素用逗号隔开，Python 就会将其视为元组
需要注意的一点是，当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号,，否则 Python 解释器会将它视为字符串
除了使用( )创建元组外，Python 还提供了一个内置的函数 tuple()，用来将其它数据类型转换为元组类型。tuple(data)
"""
yuanzu =3,4,5,6
print(yuanzu)
print(type(('1',[2,3])))

a = ('sd',)
print(a)

tup1 = "dsfag"
print(tuple(tup1))

list2 = ['f','g','gf']
print(tuple(list2))

"""
Python 字典（dict）是一种无序的、可变的序列，它的元素以“键值对（key-value）”的形式存储。
相对地，列表（list）和元组（tuple）都是有序的序列，它们的元素在底层是挨着存放的。
Python创建字典
"""

#使用字符串作为key
dict1 = {"a":"aa","b":"bb"}
dic = dict(dict1)
print(dic.get("a"))

#使用元组和数字作为key
dict1 = {(20, 30): 'great', 30: [1,2,3]}
print(dict1)
#创建空元组
dict2 = {}
print(dict2)

#2) 通过 fromkeys() 方法创建字典 dictname = dict.fromkeys(list，value=None)
# list 参数表示字典中所有键的列表（list）；value 参数表示默认值，如果不写，则为空值 None。

listlie = ['数学','英语']
print(dict.fromkeys(listlie,70))

#3) 通过 dict() 映射函数创建字典
#方式1
demo = [('two',2), ('one',1), ('three',3)]
a = dict(demo)
print(a)
#方式2
demo = [['two',2], ['one',1], ['three',3]]
#方式3
demo = (('two',2), ('one',1), ('three',3))
#方式4
demo = (['two',2], ['one',1], ['three',3])
a = dict(demo)
print(a)

keys = ['one', 'two', 'three'] #还可以是字符串或元组
values = [1, 2, 3] #还可以是字符串或元组
a = dict( zip(keys, values) ) #通过应用 dict() 函数和 zip() 函数，可将前两个列表转换为对应的字典。
print(a)

"""
注意，无论采用以上哪种方式创建字典，字典中各元素的键都只能是字符串、元组或数字，不能是列表。列表是可变的，不能作为键。
"""
print(a.get("two"))
print(a["two"]) #键不存在会抛出异常

#判断字典中是否存在指定键值对 对于 dict 而言，in 或 not in 运算符都是基于 key 来判断的。

a = {'数学': 95, '语文': 89, '英语': 90}
print("数学" in a)

'''
，Python 字典的数据类型为 dict，我们可使用 dir(dict) 来查看该类型包含哪些方法，例如：
>>> dir(dict)
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''
"""
keys()、values() 和 items() 方法
keys() 方法用于返回字典中的所有键（key）；
values() 方法用于返回字典中所有键对应的值（value）；
items() 用于返回字典中所有的键值对（key-value）。
需要注意的是，在 Python 2.x 中，上面三个方法的返回值都是列表（list）类型。
但在 Python 3.x 中，它们的返回值并不是我们常见的列表或者元组类型，因为 Python 3.x 不希望用户直接操作这几个方法的返回值。
"""
scores = {'数学': 95, '语文': 89, '英语': 90}
print(scores.keys())
print(scores.values())
print(scores.items())

"""
在 Python 3.x 中如果想使用这三个方法返回的数据，一般有下面两种方案：
"""
#1) 使用 list() 函数，将它们返回的数据转换成列表，例如：
print(list(scores.keys()))

#2) 使用 for in 循环遍历它们的返回值，例如

for k in scores.keys():
    print(k,end=' ')
print("\n")
for k in scores.values():
    print(k,end=' ')
print("\n")
for k,v in scores.items():
    print("key",k,"value",v)

'''
pop() 和 popitem() 都用来删除字典中的键值对，不同的是，
pop() 用来删除指定的键值对，而 popitem() 用来随机删除一个键值对，它们的语法格式如下：
dictname.pop(key)  dictname 表示字典名称，key 表示键。
dictname.popitem()
setdefault() 方法 setdefault() 方法用来返回某个 key 对应的 value，其语法格式如下：
dictname.setdefault(key, defaultvalue)
说明，dictname 表示字典名称，key 表示键，defaultvalue 表示默认值（可以不写，不写的话是 None）。
'''
a = {'数学': 95, '语文': 89, '英语': 90}
print(a)
#key不存在，指定默认值
a.setdefault('物理', 94)
print(a)
#key不存在，不指定默认值
a.setdefault('化学')
print(a)
#key存在，指定默认值
a.setdefault('数学', 100)
print(a)

"""
Python 中的集合，和数学中的集合概念一样，用来保存不重复的元素，即集合中的元素都是唯一的，互不相同。
从形式上看，和字典类似，Python 集合会将所有元素放在一对大括号 {} 中，相邻元素之间用“,”分隔，如下所示：
{element1,element2,...,elementn} 其中，elementn 表示集合中的元素，个数没有限制。
从内容上看，同一集合中，只能存储不可变的数据类型，包括整形、浮点型、字符串、元组，无法存储列表、字典、集合这些可变的数据类型，
否则 Python 解释器会抛出 TypeError 错误
并且需要注意的是，数据必须保证是唯一的，因为集合对于每种数据元素，只会保留一份
>>> {1,2,1,(1,2,3),'c','c'}
{1, 2, 'c', (1, 2, 3)}
其实，Python 中有两种集合类型，一种是 set 类型的集合，另一种是 frozenset 类型的集合，
它们唯一的区别是，set 类型集合可以做添加、删除元素的操作，而 forzenset 类型集合不行。
"""
#1使用 {} 创建
a = {'a','b',(1,2,3),'a'}
print(a)
#2set()函数创建集合 set() 函数为 Python 的内置函数，其功能是将字符串、列表、元组、range 对象等可迭代对象转换成集合
a = ['a','b','a',('s','f',2)]
print(set(a))
#注意，如果要创建空集合，只能使用 set() 函数实现。因为直接使用一对 {}，Python 解释器会将其视为一个空字典。
#和其他序列类型一样，手动函数集合类型，也可以使用 del() 语句，

"""
向 set 集合中添加元素
需要注意的是，使用 add() 方法添加的元素，只能是数字、字符串、元组或者布尔类型（True 和 False）值，
不能添加列表、字典、集合这类可变的数据，否则 Python 解释器会报 TypeError 错误
"""
a ={1,2,3,4}
a.add((3,4))
print(a)

"""
删除现有 set 集合中的指定元素，可以使用 remove() 方法
使用此方法删除集合中元素，需要注意的是，如果被删除元素本就不包含在集合中，则此方法会抛出 KeyError 错误。
如果我们不想在删除失败时令解释器提示 KeyError 错误，还可以使用 discard() 方法，此方法和 remove() 方法的用法完全相同，
唯一的区别就是，当删除集合中元素失败时，此方法不会抛出任何错误。
"""
a ={1,2,3,4}
a.remove(1)
print(a)
a.discard(1)
print(a)

"""
Python set集合做交集、并集、差集运算
set1={1,2,3} 和 set2={3,4,5}
交集	&	取两集合公共的元素	>>> set1 & set2
{3}
并集	|	取两集合全部的元素	>>> set1 | set2
{1,2,3,4,5}
差集	-	取一个集合中另一集合没有的元素	>>> set1 - set2
{1,2}
>>> set2 - set1
{4,5}
对称差集	^	取集合 A 和 B 中不属于 A&B 的元素	>>> set1 ^ set2
{1,2,4,5}
"""
set1 = {'a','b','c'}
set2 = {'b','d','f'}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set1 ^ set2)

"""
Python set集合方法详解
>>> dir(set)
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""
# difference() set3 = set1.difference(set2) 将 set1 中有而 set2 没有的元素给 set3
set3 = set1.difference(set2)
print(set3)
# difference_update() set1.difference_update(set2)	从 set1 中删除与 set2 相同的元素
#discard()	set1.discard(elem)	删除 set1 中的 elem 元素
#set1.discard('a')
#print(set1)
#intersection()	 set3 = set1.intersection(set2)	取 set1 和 set2 的交集给 set3
#intersection_update() set1.intersection_update(set2)	取 set1和 set2 的交集，并更新给 set1
#isdisjoint()	set1.isdisjoint(set2)	判断 set1 和 set2 是否没有交集，有交集返回 False；没有交集返回 True
#issubset()	set1.issubset(set2)	判断 set1 是否是 set2 的子集
#set1 = {1,2}
#set2 = {1,2,3}
#print(set1.issubset(set2))
#issuperset()	set1.issuperset(set2)	判断 set2 是否是 set1 的子集
#pop()	a = set1.pop()	取 set1 中一个元素，并赋值给 a
# a = set1.pop()
# print(a)
# symmetric_difference()	set3 = set1.symmetric_difference(set2)	取 set1 和 set2 中互不相同的元素，给 set3
#symmetric_difference_update()	set1.symmetric_difference_update(set2)	取 set1 和 set2 中互不相同的元素，并更新给 set1
# union()	set3 = set1.union(set2)	取 set1 和 set2 的并集，赋给 set3
# update()	set1.update(elem)	添加列表或集合中的元素到 set1

"""
Python frozenset集合（set集合的不可变版本）
set 集合是可变序列，程序可以改变序列中的元素；frozenset 集合是不可变序列，程序不能改变序列中的元素。set 集合中所有能改变集合本身的方法，
比如 remove()、discard()、add() 等，frozenset 都不支持；set 集合中不改变集合本身的方法，fronzenset 都支持。
两种情况下可以使用 fronzenset：
当集合的元素不需要改变时，我们可以使用 fronzenset 替代 set，这样更加安全。
有时候程序要求必须是不可变对象，这个时候也要使用 fronzenset 替代 set。比如，字典（dict）的键（key）就要求是不可变对象。
"""
s = {'Python', 'C', 'C++'}
fs = frozenset(['Java', 'Shell'])
print(fs)
s_sub = {'PHP', 'C#'}
#向set集合中添加frozenset
s.add(fs)
print('s =', s)
#向为set集合添加子set集合
# s.add(s_sub)
# print('s =', s)
#需要注意的是，set 集合本身的元素必须是不可变的， 所以 set 的元素不能是 set，只能是 frozenset。第 6 行代码向 set 中添加 frozenset 是没问题的，
# 因为 frozenset 是不可变的；但是，第 10 行代码中尝试向 set 中添加子 set，这是不允许的，因为 set 是可变的。