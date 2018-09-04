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