"""
Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped
over it's main diagonal, switching the row and
column indices of the matrix.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Note:

1.1 <= A.length <= 1000
2.1 <= A[0].length <= 1000
"""

# 整体思路
# 1. 首先将矩阵的行数保存为列数，列数保存为行数
# 2. 再通过append方法重新进行数组的保存，其中res.append([])可以保证正确的进行数组的保存

# 参考答案
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for j in range(len(A[0])):
            res.append([])
            for i in range(len(A)):
                res[j].append(A[i][j])
        return res


A = [[1 , 2, 3], [4, 5, 6]]
X = Solution()
Y = X.transpose(A)
print(Y)

# 更加简洁的参考答案
# class Solution:
#     def transpose(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

# 错误答案——没有考虑到rows、cols的大小不同的情况
# class Solution:
#     def transpose(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         rows = len(A)
#         cols = len(A[0])
#         for row in range(rows):
#             for col in range(cols):
#                 if col >= row:
#                     A[row][col],A[col][row] = A[col][row],A[row][col]
#         return A



