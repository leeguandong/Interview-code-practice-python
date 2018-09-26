# 每隔 k 个就逆序，用栈结构

def reverseNode(head, k):
    def reverse(stack, pre, next):
        while stack:
            cur = stack.pop()
            if pre != None:
                cur = cur.next
            pre = cur
        # pre.next = next
        return pre

    if head == None or head.next == None or k < 2:
        return head
    stack = []
    cur = head
    newHaed = head
    pre = None
    while cur != None:
        next = cur.next
        stack.append(cur)
        if len(stack) == k:
            pre = reverse(stack, pre, next)
            newHead = cur if newHaed == head else newHaed
        cur = next
    return newHaed
