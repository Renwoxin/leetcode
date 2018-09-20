"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
# import list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):

    def __init__(self):
        self.val = None
        self.next = None

    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

class ListNode_handle:
    def __init__(self):
        self.cur_node = None  # 可以理解为头指针

    def add(self, data):
        """头插法"""
        #add a new node pointed to previous node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next

    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev  # 将curr.next保存为prev，且循环保存之前的prev
            prev = curr
        return prev


if __name__ == '__main__':
    node_list = [1, 2, 3, 4, 5]
    h = ListNode_handle()
    # node = ListNode()

    for i in node_list:  # 循环向链表中加入Node
        h.add(i)
    # 头插法形成的链表顺序是5->4->3->2->1

    print('第一个结点值：', h.cur_node.val)
    print('第二个结点值：', h.cur_node.next.val)
    print('...')
    print("--" * 50)

    C = Solution()
    D = C.reverseList(h.cur_node)
    print('返回的第一个结点值：', D.val)
    print('返回值的类型：', type(D))
    print("--" * 50)

    node_list_reverse = node_list[::-1]
    print("输入链表顺序：", node_list_reverse)
    print("输出链表顺序： ", end=' ')
    while D.next:
        print(D.val, end=' ')
        D = D.next
    print(D.val)