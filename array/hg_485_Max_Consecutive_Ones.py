"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

1. The input array will only contain 0 and 1.
2. The length of input array is a positive integer and will not exceed 10,000
"""
# 整体思路
# 1.首先计算出每一个连续'1'段的连续大小
# 2.将这些值放入一个数组中，降序排序之后，输出第一个值
# max() 方法返回给定参数的最大值，参数可以为序列。

# 参考答案
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = 0
        maxn = 0
        for i,v in enumerate(nums):
            if v == 1:
                n += 1
            else:
                maxn = max(maxn, n)
                n = 0
        maxn = max(maxn, n)
        return maxn


# by myself
# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = []
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 count += 1
#             else:
#                 res.append(count)
#                 count = 0
#         res.append(count)
#         res.sort(reverse=True)
#         return res[0]


A = [1, 1, 0, 1, 1, 1]
B = Solution()
print(B.findMaxConsecutiveOnes(A))