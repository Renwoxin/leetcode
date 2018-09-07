"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with
different size but keep its original data.You're given a matrix represented by a two-dimensional array, and
two positive integers r and c representing the row number and column number of the wanted reshaped matrix,
respectively.The reshaped matrix need to be filled with all the elements of the original matrix in the same
row-traversing order as they were.If the 'reshape' operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix,fill it row by row by
using the previous list.

Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
1. The height and width of the given matrix is in range [1, 100].
2. The given r and c are all positive.
"""
# 整体思路
# 1.首先将矩阵按照行读取保存为1*len(nums)
# 2.重新按照需要定义的矩阵的大小重新保存图片

# by myself
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if (r * c) != (len(nums) * len(nums[0])):
            return nums
        nums = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
        res = []
        k = 0
        for i in range(r):
            res.append([])
            for j in range(c):
                res[i].append(nums[k])
                k += 1
        return res

# 参考答案
# class Solution:
#     def matrixReshape(self, nums, r, c):
#         """
#         :type nums: List[List[int]]
#         :type r: int
#         :type c: int
#         :rtype: List[List[int]]
#         """
#         if len(nums) * len(nums[0]) != r * c: return nums # check
#         l = [n for num in nums for n in num] # flatten 2-d array -> 1-d array
#         return [l[i: i+c] for i in range(0, len(l), c)] # reshape vector -> matrix

A = [[1,1,0,0],
     [1,0,0,1],
     [0,1,1,1],
     [1,0,1,0]]
X = Solution()
Y = X.matrixReshape(A,2,8)
print(Y)