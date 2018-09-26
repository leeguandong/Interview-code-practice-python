def remove(head, num):
    if head == None:
        return None
    stack = []
    while head != None:
        if head.val != num:
            stack.append(head)
        head = head.next
    while stack:
        # 这是一个链接操作
        stack[-1].next = head
        head = stack.pop()
    return head
