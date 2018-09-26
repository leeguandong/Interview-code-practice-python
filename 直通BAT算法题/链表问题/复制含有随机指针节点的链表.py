class RandNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.rand = None

def copyListWithRand(head):
    if head == None:
        return None
    map = {}
    cur = head
    while cur != None:
        map[cur] = RandNode(cur.val)
        cur = cur.next
    cur = head
    while cur != None:
        map[cur].next = None if cur.next == None else map[cur.next]
        map[cur].next = None if cur.ramd == None else map[cur.rand]
        cur = cur.next
    return map[head]
