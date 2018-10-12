"""
We have two special characters. The first character can be represented by one bit 0. The second character can be
represented by two bits (10 or 11).Now given a string represented by several bits. Return whether the last
character must be a one-bit character or not. The given string will always end with a zero.


Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:

1.1 <= len(bits) <= 1000.
2.bits[i] is always 0 or 1.
"""

# 整体思路　
# 首先判断bits是否为空
# 若不为空，在根据具体要求逐个判断每一对是否满足需求
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits: return False
        n = len(bits)

        index = 0
        while index < n:
            if index == n - 1: return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return False


A = [1, 1, 0]
B = Solution()
print(B.isOneBitCharacter(A))