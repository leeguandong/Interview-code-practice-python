class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

def getloopmeet(head):
    fast = head.next
    slow = head.next.next
    while fast != slow:
        if fast != None or slow != None:
            return None
        fast = fast.next.next
        slow = slow.next
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.fast
    return fast
