<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [array](#array)
	- [row为一个一维列表](#row为一个一维列表)
	- [A为一个二维矩阵](#a为一个二维矩阵)
	- [set()](#set)

<!-- /TOC -->
# array

## row为一个一维列表

+ row[~i] = row[-i-1] = row[len(row) - 1 - i]
+ a,b = b,a——python中的交换变量值
+ row[i] ^ 1 —— row[i] 与 1 进行按位异或

## A为一个二维矩阵
```python
  # 转置
  [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
  # 按列取元素
  [A[i][j] for i in range(len(A)) for j in range(len(A[0]))]
```

## set()
+ set()函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等

```python
In [1]: a = [1,2,3]
In [2]: set(a)
Out[2]: {1, 2, 3}
In [3]: a = [1,2,3,1]
In [4]: set(a)
Out[4]: {1, 2, 3}
In [5]: x = set('runoob')
In [6]: x
Out[6]: {'b', 'n', 'o', 'r', 'u'}
```

## sort()

### 语法
+ list.sort(cmp=None, key=None, reverse=False)

### 参数

+ 深入利用list.sort()函数
+ cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
+ key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
+ reverse -- 排序规则，reverse = True降序， reverse = False 升序（默认）。

```python
In [1]: A = [3, 2, 1, 4]
In [2]: A.sort(key = lambda x:x%2)
In [3]: A
Out[3: [2, 4, 3, 1]
```

## max()
+ max() 方法返回给定参数的最大值，参数可以为序列。

##＃ 语法
+ max( x, y, z, .... )

##＃ 参数
+ x -- 数值表达式。
+ y -- 数值表达式。
+ z -- 数值表达式。

##＃ 返回值
+ 返回给定参数的最大值。

##＃ 例子
```python
In [1]: max(80, 100, 1000)
Out[1]: 1000
```
