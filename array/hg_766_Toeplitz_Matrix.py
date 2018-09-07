"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

1.matrix will be a 2D array of integers.
2.matrix will have a number of rows and columns in range [1, 20].
3.matrix[i][j] will be integers in range [0, 99].
"""

# 整体思路
# 1. 根据题目性质判断出是寻找matrix[i][j]与matrix[i+1][j+1]是否相等
# 2. 由于矩阵的性质，所以不需要遍历行尾和列尾，故有len(matrix)-1和len(matrix[0])-1

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

# 参考答案
# 1.先定义一个字典保存矩阵中的数且同样的数只保存一次
# 2.再判断对应的数是否与字典中所对应的数相同（在key相同的情况下）
# class Solution(object):
#     def isToeplitzMatrix(self, matrix):
#         groups = {}
#         for r, row in enumerate(matrix):
#             for c, val in enumerate(row):
#                 if r-c not in groups:
#                     groups[r-c] = val
#                 elif groups[r-c] != val:
#                     return False
#         return True


# class Solution(object):
#     def isToeplitzMatrix(self, matrix):
#         return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
#                    for r, row in enumerate(matrix)
#                    for c, val in enumerate(row))

A = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
X = Solution()
Y = X.isToeplitzMatrix(A)
print(Y)