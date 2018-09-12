# """
# You're given strings J representing the types of stones that are jewels, and S representing the
# stones you have.  Each character in S is a type of stone you have.  You want to know how many
# of the stones you have are also jewels.The letters in J are guaranteed distinct, and all
# characters in J and S are letters. Letters are case sensitive, so "a" is considered a different
# type of stone from "A".
#
# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
# Example 2:
#
# Input: J = "z", S = "ZZ"
# Output: 0
#
# Note:
#
# 1. S and J will consist of letters and have length at most 50.
# 2. The characters in J are distinct.
# """

# # 整体思路
# # 循环遍历S中的字符串
# # 判断S中的元素是否在J中，并计数，返回计数值
# # map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
# 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list

# class Solution:
#     def numJewelsInStones(self, J, S):
#         """
#         :type J: str
#         :type S: str
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(S)):
#             if S[i] in J:
#                 count += 1
#         return count
#


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(map(J.count, S))


J = "z"
S = "ZZ"
num = Solution()
JS = num.numJewelsInStones(J,S)
print(JS)

# from collections import Iterable
# J = '12'
# S = '1123456789'
# print(sum(map(J.count, S)))
# print("*"*20)
#
# print(isinstance(map(J.count, S), Iterable))
# print("*"*20)
#
# X = map(J.count, S)
# for i in X:
#     print(i)
# print("*"*20)
#
# print(J.count('1'))
# print(J.count('2'))
# print(J.count('3'))
# print(J.count('4'))
# print(J.count('5'))
# print(J.count('6'))
# print(J.count('7'))
# print(J.count('8'))
# print(J.count('9'))