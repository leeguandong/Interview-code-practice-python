'''
题目：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

'''
方法一：递归版本，注意比较很好理解
30ms
5670k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        mergepHead = None
        if pHead1.val <= pHead2.val:
            mergepHead = pHead1
            mergepHead.next = self.Merge(pHead1.next, pHead2)
        elif pHead1.val > pHead2.val:
            mergepHead = pHead2
            mergepHead.next = self.Merge(pHead1, pHead2.next)

        return mergepHead

'''
版本二：非递归版本
23ms
5676k
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        dummy = ListNode(0)
        pHead = dummy

        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                dummy.next = pHead2
                pHead2 = pHead2.next
            else:
                dummy.next = pHead1
                pHead1 = pHead1.next

            dummy = dummy.next
        if pHead1:
            dummy.next = pHead1
        elif pHead2:
                dummy.next = pHead2
        return pHead.next