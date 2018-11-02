"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


#　by myself 超时了
# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         k = 0
#         res = sum(nums)
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 res = max(res, sum(nums[k:k+j+1]))
#             k += 1
#         return res


A = [-2,1,-3,4,-1,2,1,-5,4]
X = Solution()
Y = X.maxSubArray(A)
print(Y)