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
