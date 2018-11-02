"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

1. If the two linked lists have no intersection at all, return null.
2. The linked lists must retain their original structure after the function returns.
3. You may assume there are no cycles anywhere in the entire linked structure.
4. Your code should preferably run in O(n) time and use only O(1) memory.
"""
import list
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None

        # Concatenate A and B
        last = headA
        while last.next: last = last.next
        last.next = headB

        # Find the start of the loop
        fast = slow = headA
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = headA
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow

        # No loop found
        last.next = None
        return None



if __name__ == '__main__':
    node_list1 = [9, 8, 7, 2, 1]
    node_list2 = [9, 8, 7, 4, 3, 2]
    l1 = list.ListNode_handle()
    l2 = list.ListNode_handle()
    for i in node_list1:
        l1.add(i)
    for i in node_list2:
        l2.add(i)
    A = Solution()
    B = A.getIntersectionNode(l1.cur_node,l2.cur_node)
    while B.next:
        print(B.val, end='')
        B = B.next
    print(B.val)