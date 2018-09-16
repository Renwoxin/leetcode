"""
Given an integer array with even length, where different numbers in this array represent different
kinds of candies. Each number means one candy of the corresponding kind. You need to distribute
these candies equally in number to brother and sister. Return the maximum number of kinds of
candies the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.

Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.

Note:

1. The length of the given array is in range [2, 10,000], and will be even.
2. The number in given array is in range [-100,000, 100,000].
"""
# 整体思路
# 要考虑的是sister分到的糖果最大的类别，而输入首先必须是平均的，
# 如果有一类是单数，那么必然是分给sisiter，所以通过set函数求类
# 别再与candies的二分之一比较可以得到结果

#参考答案
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        n = len(candies) / 2
        s = len(set(candies))
        if s < n:
            return s
        else:
            return int(n)

candies = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
A = Solution()
print(A.distributeCandies(candies))