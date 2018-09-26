# 在环外面就相交，或者在环上相交（可能在同一个交点上，可能不在同一个交点上）

def bothLoop(head1, node1, head2, node2):
    if head1 == None or head2 == None:
        return None
    if node1 == node2:
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1 != node1:
            n += 1
            cur1 = cur1.next
        while cur2 != node2:
            n -= 1
            cur2 = cur2.next
        if cur1 != cur2:
            return None
        cur1 = head1 if n >= 0 else head2
        cur2 = head1 if cur1 == head2 else head2
        n = abs(n)
        while n != 0:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = node1.next
        while cur1 != node1:
            if cur1 == node2:
                return node1
            cur = cur1.next
        return None

def noLoop(head1, head2):
    if head1 == None or head2 == None:
        return None
    cur1 = head1
    cur2 = head2
    n = 0
    while cur1.next != None:
        n += 1
        cur1 = cur1.next
    while cur2.next != None:
        n -= 1
        cur2 = cur2.next
    if cur1 != cur2:
        return None
    cur1 = head1 if n >= 0 else head2
    cur2 = head1 if cur1 == head2 else head2
    n = abs(n)
    while n != 0:
        cur1 = cur1.next
        n -= 1
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

def getLoopNode(head):
    if head == None or head.next == None or head.next.next == None:
        return None
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if fast.next == None or fast.next.next == None:
            return None
        slow = slow.next
        fast = fast.next.next
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def getIntersectNode(head1, head2):
    if head1 == None or head2 == None:
        return None
    # 判断环的入口在哪里
    node1 = getLoopNode(head1)
    node2 = getLoopNode(head2)
    if node1 == None and node2 == None:
        return noLoop(head1, head2)
    # 在环之前就相等，node1 = node2，在环中相等，
    if node1 != None and node2 != None:
        return bothLoop(head1, node1, head2, node2)
    return None
