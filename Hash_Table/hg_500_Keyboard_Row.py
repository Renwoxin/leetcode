"""
Given a List of words, return the words that can be typed using letters of alphabet on
only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
1.You may use one character in the keyboard more than once.
2.You may assume the input string will only contain letters of alphabet.
"""

# 整体思路
# 首先要明白题意，题中涉及到输入是“words”
# 1. 根据美式键盘定义3个字符串
# 2. 判断输入的word是否在3个字符串中，如果是则保存在列表中
# str.upper()——将字符串中的小写字母转为大写字母
# set.issubset() ——   def issubset(self, s: Iterable) -> bool
#                     Report whether another set contains this set.

# by myself
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        S1 = "QWERTYUIOP"
        S2 = "ASDFGHJKL"
        S3 = "ZXCVBNM"

        Set1 = set(S1)
        Set2 = set(S2)
        Set3 = set(S3)

        res = []
        for word in words:
            word_new = word.upper()
            if all(word_new[i] in Set1 for i in range(len(word_new))) or \
                    all(word_new[i] in Set2 for i in range(len(word_new))) or \
                    all(word_new[i] in Set3 for i in range(len(word_new))):
                res.append(word)
        return res


# 参考答案
# class Solution:
#     def findWords(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         set1 = {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"}
#         set2 = {"A", "S", "D", "F", "G", "H", "J", "K", "L"}
#         set3 = {"Z", "X", "C", "V", "B", "N", "M"}
#
#         res = []
#         for word in words:
#             test_set = set(word.upper())
#             if test_set.issubset(set1) or test_set.issubset(set2) or test_set.issubset(set3):
#                 res.append(word)
#         return res

# set.issubset() ——   def issubset(self, s: Iterable) -> bool
#                     Report whether another set contains this set.
A = Solution()
B = ["Hello", "Alaska", "Dad", "Peace"]
C = A.findWords(B)
print(C)