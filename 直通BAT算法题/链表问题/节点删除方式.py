# 链表里删元素，但是不知道元素的头结点和链表本身结构
def dele(node):
    if node == None:
        return None
    next = node.next
    if next == None:
        return []
    node.val = next.val
    node.next = next.next
