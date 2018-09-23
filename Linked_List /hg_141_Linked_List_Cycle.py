"""
Given a linked list, determine if it has a cycle in it.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解题思路：快慢指针技巧，slow指针和fast指针开始同时指向头结点head，fast每次走两步，
# slow每次走一步。如果链表不存在环，那么fast或者fast.next会先到None。
# 如果链表中存在环路，则由于fast指针移动的速度是slow指针移动速度的两倍，
# 所以在进入环路以后，两个指针迟早会相遇，如果在某一时刻slow==fast，说明链表存在环路。

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
