"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#考虑到单链表缺失从后向前的信息，如果能得到双向信息将很容易判断回文。
# 故考虑将单链表的节点值记录到一个数组中，判断数组是否回文；
# 或通过一次遍历将单链表拓展成双向链表，再判断是否回文。

# 代码（时间 O(n)，空间O(n)）


import list
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        tmp_list = []
        while head:
            tmp_list.append(head.val)
            head = head.next

        length = len(tmp_list)
        for i in range(int(length / 2)):
            if tmp_list[i] != tmp_list[length - i - 1]:
                return False
        return True


if __name__ == '__main__':
    node_list = [1, 2, 2, 1]
    l = list.ListNode_handle()

    for i in node_list:
        l.add(i)
    A = Solution()
    B = A.isPalindrome(l.cur_node)
    print(B)