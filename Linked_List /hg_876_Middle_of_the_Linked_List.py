"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:

The number of nodes in the given list will be between 1 and 100.
"""

# # Definition for singly-linked list.
import list


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head


if __name__ == '__main__':
    node_list = [7, 6, 5, 4, 3, 2, 1]
    h = list.ListNode_handle()
    # node = ListNode()

    for i in node_list:  # 循环向链表中加入Node
        h.add(i)
    # 头插法形成的链表顺序是1->2->3->4->5

    print('第一个结点值：', h.cur_node.val)
    print('第二个结点值：', h.cur_node.next.val)
    print('...')
    print("--" * 50)

    C = Solution()
    D = C.middleNode(h.cur_node)
    print('返回的第一个结点值：', D.val)
    print('返回值的类型：', type(D))
    print("--" * 50)

    print("输出链表顺序： ", end=' ')
    while D.next:
        print(D.val, end=' ')
        D = D.next
    print(D.val)