'''
题目：输入一个链表，反转链表后，输出链表的所有元素。
'''

'''
这一题还是蛮难的。链表的翻转，例如 1->2->3->4->5  ==>  5->4->3->2->1
tmp = pHead.next   把当前节点的下一个节点保存下来
pHead.next = pre   把前一个节点移到当前节点的下一个节点，因为要翻转节点，pre始终指向要反转节点的首节点
pre = pHead        当前节点向后移一位
pHead = tmp        把之前保存的下一个节点指针再给当前节点接着翻转
33ms
6016k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pre = None
        while pHead:
            tmp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = tmp
        return pre



