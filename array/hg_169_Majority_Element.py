"""
Given an array of size n, find the majority element. The majority element is the element that
appears more than ⌊ n/2 ⌋ times.You may assume that the array is non-empty and the majority
element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

# 整体思路
# 首先利用Ｃｏｕｎｔｅｒ函数计算出每一个element的个数
# 然后比较大小，找出计数个数最大的element，并且输出
# by myself
# import collections
#
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         counts = collections.Counter(nums)
#         count = 0
#         res = 0
#         for i in counts:
#             if counts[i] >= count:
#                 count = counts[i]
#                 res = i
#         return res

# 参考答案
import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        res = max(counts.keys(), key=counts.get)
        return res

A = [3,3,4]
B = Solution()
print(B.majorityElement(A))