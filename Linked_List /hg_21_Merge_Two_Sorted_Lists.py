"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

#　整体思路
#　递归
# 问题：　return l1 or l2 有什么具体功能？还能一直循环返回？
import list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l = None
        # prev = None
        # while l1 or l2:
        #     if l1:
        #         curr1 = l1
        #         l1 = l1.next
        #         curr1.next = l
        #         l = curr1
        #     if l2:
        #         curr1 = l2
        #         l2 = l2.next
        #         curr1.next = l
        #         l = curr1
        # while l:
        #     curr2 = l
        #     l = l.next
        #     curr2.next = prev
        #     prev = curr2
        # return prev
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

if __name__ == '__main__':
    node_list1 = [5, 3, 1]
    node_list2 = [4, 2, 1]
    l1 = list.ListNode_handle()
    l2 = list.ListNode_handle()

    for i in node_list1:
        l1.add(i)
    for i in node_list2:
        l2.add(i)

    A = Solution()
    B = A.mergeTwoLists(l1.cur_node, l2.cur_node)
    while B.next:
        print(B.val, end=' ')
        B = B.next
    print(B.val)