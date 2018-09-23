"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 问题：为什么head可以变化？
import list
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        node = head

        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head


if __name__ == '__main__':
    node_list = [2, 2, 1, 1]
    l = list.ListNode_handle()

    for i in node_list:
        l.add(i)
    A = Solution()
    B = A.deleteDuplicates(l.cur_node)
    while B.next:
        print(B.val, end=' ')
        B = B.next
    print(B.val)