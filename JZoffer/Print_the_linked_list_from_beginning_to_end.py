"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""

# 递归

import list
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):

        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]


node_list1 = [3, 2, 1]
l1 = list.ListNode_handle()
for i in node_list1:
    l1.add(i)


A = Solution()
B = A.printListFromTailToHead(l1.cur_node)

print(B)
