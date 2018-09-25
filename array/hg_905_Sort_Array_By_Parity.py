"""
Given an array A of non-negative integers, return an array consisting of all
the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1. 1 <= A.length <= 5000
2. 0 <= A[i] <= 5000
"""
# 深入利用list.sort()函数
# cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True降序， reverse = False 升序（默认）。

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key=lambda x: x % 2)
        return A

A = [3, 1, 2, 6]
B = Solution()
print(B.sortArrayByParity(A))