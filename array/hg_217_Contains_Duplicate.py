"""
Given an array of integers, find if the array contains any duplicates
Your function should return true if any value appears at least twice in
the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
# 整体思路
# 巧妙利用set()函数
# by myself
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sets = set(nums)
        if len(sets) == len(nums):
            return False
        else:
            return True
        # 参考答案
        # return len(nums) != len(set(nums))

A = [1,1,1,3,3,4,3,2,4,2]
B = Solution()
print(B.containsDuplicate(A))