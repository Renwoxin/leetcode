"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the
resulting image.To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].To invert an image means that
each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results
in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Notes:
1.1 <= A.length = A[0].length <= 20
2.0 <= A[i][j] <= 1
"""
# 整体思路
# 1. 先将数组进行行对称
# 2. 再对每个元素进行取反

# 参考答案有一些很实用的方法
# row[~i] = row[-i-1] = row[len(row) - 1 - i]
# a,b = b,a——python中的交换变量值
# row[i] ^ 1 —— row[i] 与 1 进行按位异或
# 标准答案
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in range(int((len(row) + 1) / 2)):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
"""
Complexity Analysis

Time Complexity: O(N)O(N), where N is the total number of elements in A.
Space Complexity: O(1)O(1) in additional space complexity.
"""

A = Solution()
B = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
C = A.flipAndInvertImage(B)
print(C)
# 网上参考答案
# class Solution:
#     def flipAndInvertImage(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         rows = len(A)
#         cols = len(A[0])
#         for row in range(rows):
#             A[row] = A[row][::-1]
#             for col in range(cols):
#                 A[row][col] ^= 1
#         return A


# # 错误答案，但是还是有点用 by myself
# 程序中求取m,n的方法可以用len()代替
# 向上取整可以用int(n/2+1)代替

# import numpy as np
# import math
#
# A = [[1,1,0,0],[1,0,1,0],[1,0,0,0]]
#
# m,n = np.shape(A)
#
# for i in range(m):
#     for j in range(math.ceil(n/2)):
#         a = A[i][j]
#         A[i][j] = A[i][n-j-1]
#         A[i][n-j-1] = a
# print(A)
#
# m,n = np.shape(A)
#
# for i in range(m):
#     for j in range(n):
#         if A[i][j] == 0:
#             A[i][j] = 1
#         else:
#             A[i][j] = 0
# print(A)