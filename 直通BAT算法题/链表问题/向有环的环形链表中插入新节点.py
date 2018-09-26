# 指针给的是节点值
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def insertnum(head, num):
        node = Node(num)
        if head == None:
            node.next = node
            return node
        node = head
        pre = node
        cur = node.next
        while cur != head:
            if pre.value > num and cur.value <= num:
                break
            pre = pre.next
            cur = cur.next
        # num 小于节点值，pre只跑到最后一个节点，node跑道头结点
        pre.next = node
        node.next = cur
        # 是按顺序来的，返回的是 head 或者 node ，是有顺序决定的
        return head if head.value < num else node

node = Node()
node.insertnum([[1, 2, 3], 5])
