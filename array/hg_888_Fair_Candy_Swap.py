"""
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has,
and B[j] is the size of the j-th bar of candy that Bob has.Since they are friends, they would like to exchange
one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total
amount of candy a person has is the sum of the sizes of candy bars they have.) Return an integer array ans
where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar
that Bob must exchange.If there are multiple answers, you may return any one of them.  It is guaranteed an
answer exists.

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]
Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]
Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]


Note:

1.1 <= A.length <= 10000
2.1 <= B.length <= 10000
3.1 <= A[i] <= 100000
4.1 <= B[i] <= 100000
5.It is guaranteed that Alice and Bob have different total amounts of candy.
6.It is guaranteed there exists an answer.
"""
# 整体思路
# 通过公式SA−x+y=SB−y+x (Alice and Bob have total candy SA, SB respectively；
# Alice gives candy x, and receives candy y, then Bob receives candy x and gives candy y)

# 得出 y = x + (SB - SA)/2
# 所以根据此条件来判断是否达到交换条件

class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]


# class Solution:
#     def fairCandySwap(self, A, B):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :rtype: List[int]
#         """
#         if sum(A[::1]) == sum(B[::1]) or (sum(B[::1])+sum(A[::1]))%2 != 0:
#             return False
#         for j in range(len(B)):
#             for i in range(len(A)):
#                 A[i],B[j] = B[j],A[i]
#                 if sum(A[::1]) == sum(B[::1]):
#                     return [B[j],A[i]]
#                 A[i], B[j] = B[j], A[i]

A = [1,2,5,2]
B = [2,2,4]
X = Solution()
Y = X.fairCandySwap(A,B)
print(Y)

