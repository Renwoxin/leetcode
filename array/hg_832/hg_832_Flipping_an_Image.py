# 标准答案
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in range((len(row) + 1) / 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A

# 网上参考答案
# A = [[1,1,0],[1,0,1],[0,0,0]]
# rows = len(A)
# cols = len(A[0])
# for row in range(rows):
#     A[row] = A[row][::-1]
#     for col in range(cols):
#         A[row][col] ^= 1
# print(A)


# # 错误答案 by myself
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