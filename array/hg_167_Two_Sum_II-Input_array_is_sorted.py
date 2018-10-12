"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to
a specific target number.The function twoSum should return indices of the two numbers such that they add up to
the target, where index1 must be less than index2.

Note:

1. Your returned answers (both index1 and index2) are not zero-based.
2. You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

# 整体思路
# 这道题参考答案的思路涉及到了查找方法的思想
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1



A = [3,24,50,79,88,150,345]
target = 9
B = Solution()
print(B.twoSum(A,target))