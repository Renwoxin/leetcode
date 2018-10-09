"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
# 参考答案
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        # for i in range(len(nums)):
        #     index = abs(nums[i]) - 1
        #     nums[index] = - abs(nums[index])
        #
        # return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return list(set(range(1, len(nums) + 1)) - set(nums))


#题意理解错误，所以做错了
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         nums0 = sorted(nums)
#         nums1 = []
#         res = []
#         a = 0
#         for i in range(len(nums)-1):
#             if nums0[i]+1 != nums0[i+1] and nums0[i] != nums0[i+1]:
#                 a = nums0[i+1] - nums0[i]
#                 nums1 = list(range(nums0[i]+1,nums0[i]+a,1))
#                 res.extend(nums1)
#             nums1 = []
#             a = 0
#         return res


A = [4,3,2,7,8,2,3,1]
B = Solution()
print(B.findDisappearedNumbers(A))