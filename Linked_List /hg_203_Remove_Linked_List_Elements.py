"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import list
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # node = head
        # while node.next:
        #     if node.val == val:
        #         head = head.next
        #         node = node.next
        #     else:
        #         node = node.next
        # return head
        # move the head to its next node if its value is equal to the input value
        if not head: return
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return
        curr = head
        while curr and curr.next:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return head


if __name__ == '__main__':
    node_list = [6]
    l = list.ListNode_handle()

    for i in node_list:
        l.add(i)
    A = Solution()
    B = A.removeElements(l.cur_node,6)
    while B.next:
        print(B.val, end=' ')
        B = B.next
    print(B.val)