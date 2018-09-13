## map()

+ map()是 Python 内置的高阶函数，map() 会根据提供的函数对指定序列做映射。
+ 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含
+ 每次 function 函数返回值的新列表

+ map() 函数语法：
  - map(function, iterable, ...)
  - function -- 函数
  - iterable -- 一个或多个序列

```python
def square(x) :            # 计算平方数
...     return x ** 2

map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
```
```python
from collections import Iterable
J = '12'
S = '1123456789'
print(sum(map(J.count, S)))
print("*"*20)

print(isinstance(map(J.count, S), Iterable))  # 判断map(J.count, S)是类型
print("*"*20)

X = map(J.count, S)
for i in X:
    print(i)
print("*"*20)

print(J.count('1'))
print(J.count('2'))
print(J.count('3'))
print(J.count('4'))
print(J.count('5'))
print(J.count('6'))
print(J.count('7'))
print(J.count('8'))
print(J.count('9'))
```

## isinstance()

+ isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()

+ isinstance() 与 type() 区别：
  - type() 不会认为子类是一种父类类型，不考虑继承关系。
  - isinstance() 会认为子类是一种父类类型，考虑继承关系。
  - 如果要判断两个类型是否相同推荐使用 isinstance()。

+ isinstance() 方法的语法:
  - isinstance(object, classinfo)
+ 参数
  - object -- 实例对象。
  - classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
+ 返回值
  - 如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False

```python
a = 2
isinstance (a,int)
True
```

## collections.Counter()
+ 定义一个 c = collections.Counter() ，c可以保存一系列字典
+ 通过collections.Counter可以计算一个字符串列表中每一个单词出现的次数，并以单词为key、次数为内容保存为字典形式

## split()
+ split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
+ 语法
  - str.split(str="", num=string.count(str)).
+ 参数
  - str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
  - num -- 分割次数
+ 返回值
  - 返回分割后的字符串列表

## upper()
+ upper() 方法将字符串中的小写字母转为大写字母
+ 正确用法
  - str_new = str.upper()

```python
str = "this is string example....wow!!!";
print "str.upper() : ", str.upper()

output:str.upper() :  THIS IS STRING EXAMPLE....WOW!!!
```

## set.issubset()

+ set.issubset()

```python
def issubset(self, s: Iterable) -> bool
  - Report whether another set contains this set.——判断是否为子集
```

## 字符串的拼接

```python
In [1]: A = "this apple is sweet"
In [2]: B = "this apple is sour"

In [3]: A + B
Out[3]: 'this apple is sweetthis apple is sour'

In [4]: A +" "+B
Out[4]: 'this apple is sweet this apple is sour'
```
