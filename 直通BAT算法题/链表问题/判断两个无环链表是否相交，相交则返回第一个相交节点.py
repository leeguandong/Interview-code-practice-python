class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

def Loop(head1, head2):
    n1 = 0
    n2 = 0
    cur1 = head1
    cur2 = head2
    while cur1 != None:
        n1 += 1
        cur1 = cur1.next
        print(n1)
    while cur2 != None:
        n2 += 1
        cur2 = cur2.next
        print(n2)

    n = abs(n1 - n2)
    print(n)
    cur1 = head1
    cur2 = head2
    if n1 > n2:
        while n > 0:
            cur1 = cur1.next
    else:
        while n > 0:
            cur2 = cur2.next

    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

# node1 = Node([1, 2, 3])
# node2 = Node([2, 3])
# print(Loop(node1, node2))
