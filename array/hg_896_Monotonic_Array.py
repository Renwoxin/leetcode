"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is
monotone decreasing if for all i <= j, A[i] >= A[j].Return true if and only if the
given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true

Note:

1. <= A.length <= 50000
2. -100000 <= A[i] <= 100000
"""
# python3中已经没有内置cmp()函数

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if all((A[i] >= A[i+1] for i in range(len(A)-1))) or all((A[i] <= A[i+1] for i in range(len(A)-1))):
            return True
        else:
            return False


# class Solution(object):
#     def isMonotonic(self, A):
#         """
#         :type A: List[int]
#         :rtype: bool
#         """
#         return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
#                 all(A[i] >= A[i+1] for i in range(len(A) - 1)))

# A = Solution()
# B = [0,1,1,1,1,1,1,1]
# C = A.isMonotonic(B)
# print(C)
A = [1,1,0,0,1,0,3,1]
a1 = (A[i] >= A[i+1] for i in range(len(A)-1))
a2 = (A[i] <= A[i+1] for i in range(len(A)-1))
print(a1)
print(a2)
print(all(a1))
print(all(a2))

print("**"*50)
for k in a1:
    print(k)

print("--"*50)
for k in a2:
    print(k)