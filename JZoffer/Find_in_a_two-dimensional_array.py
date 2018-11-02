"""
In a two-dimensional array (the length of each one-dimensional array is
the same), each row is sorted in ascending order from left to right, and
each column is sorted in ascending order from top to bottom. Please
complete a function, enter a two-dimensional array and an integer to
determine whether the array contains the integer.
"""

# 整体思路
# 1.题意是在一个二维数组中寻找一个target,然而该二维数组有个特点，行列都是依次递增
# 2.根据二维数组的特点，可以想到一个思路：从数组的左下角开始遍历，
# 如果小于该数字那么就往上走，如果大于该数字那么就往右走(参考大佬的思路)
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array) - 1
        cols = len(array[0]) - 1
        i = rows
        j = 0
        while j <= cols and i >= 0:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:
                return True
        return False


A = [[1,3,4],
     [2,5,8],
     [3,6,9]]
target = 5
B = Solution().Find(target,A)
print(B)