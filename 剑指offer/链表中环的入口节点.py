'''
题目：一个链表中包含环，请找出该链表的环的入口结点。
'''

'''
思路：链表指针区只能指向一个下一个节点，所以如果链表中由环一定是在尾部。
寻找链表中环的入口结点主要分成三个步骤：首先是设置两个快慢指针，如果快慢指针相遇，则快慢指针必然都在环中；
然后从相遇的地方设置一个指针向后遍历并记录走的步数，当这个指针重新指到开始的位置的时候，当前对应的步数就是
环中结点的数量k；然后设置两个指针从链表开始，第一个节点先走k步，然后第二个指针指到链表的开始，两个指针每次
都向后走一步，两个指针相遇的位置就是链表的入口。

程序可以运行，但在牛客网上报错 'NoneType' object has no attribute 'next' 不知道为什么？？
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        MeetingNode = self.MeetingNode(pHead)
        if not MeetingNode:
            return None
        NodeOfLoop = 1
        FlagNode = MeetingNode
        # 从相遇点定义一个指针，指针向后移动到相遇点即为环的节点数NodeOfLoop
        while FlagNode.next != MeetingNode:
            NodeOfLoop += 1
            FlagNode = FlagNode.next

        # 两个指针都位于首位，让其中一个节点向前走环的节点数步，然后第二个指针走，当两个指针相遇时，即为环节点入口
        pFast = pHead
        pSlow = pHead
        for i in range(NodeOfLoop):
            pFast = pFast.next
        while pSlow != pFast:
            pSlow = pSlow.next
            pFast = pFast.next
        return pFast

    # 定义快慢指针，如果有环，快慢指针一定会相遇
    def MeetingNode(self, pHead):
        if not pHead:
            return None
        pSlow = pHead.next
        pFast = pSlow.next
        while pSlow != pFast:
            pSlow = pSlow.next
            pFast = pFast.next.next
        return pSlow

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)
