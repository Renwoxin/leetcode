"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
 say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n
 as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
1.n is a positive integer, which is in the range of [1, 10000].
2.All the integers in the array will be in the range of [-10000, 10000].
"""
# 整体思路
# 1. 先将列表排序
# 2.由于是两两组合，所以以步进为2求元素之和

# 参考答案

class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])

# # 自行编写
# class Solution:
#     def arrayPairSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         sum = 0
#         for i in range(0,len(nums)-1,2):
#             sum += nums[i]
#             i += 1
#         return sum

