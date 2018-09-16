"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
# 整体思路
# 利用collections.Counter()函数计数
# 返回内容为”1“的key
# by myself

import collections
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        for i in count:
            if count[i] == 1:
                return i


nums = [4,1,2,1,2]
A = Solution()
print(A.singleNumber(nums))