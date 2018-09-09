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
