"""
We are given two sentences A and B.  (A sentence is a string of space separated words.
Each word consists only of lowercase letters.)A word is uncommon if it appears exactly
once in one of the sentences, and does not appear in the other sentence.Return a list
of all uncommon words. You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

1. 0 <= A.length <= 200
2. 0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""

# 整体思路
# 1. 通过collections.Counter可以计算一个字符串列表中每一个单词出现的次数，
# 并以单词为key、次数为内容保存为字典形式
# 2. 判断次数之后返回次数为1的key即可


# 参考答案
import collections
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]


A = "this apple is sweet"
B = "this apple is sour"
C = Solution()
D = C.uncommonFromSentences(A,B)
print(D)