class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

def compare(head1, head2):
    if head1 == None or head2 == None:
        return []

    res = []
    while head1 != None and head2 != None:
        if head1.val > head2.val:
            head2 = head2.next
        elif head1.val < head2.val:
            head1 = head1.next
        else:
            print(head1)
            res.append(head1)
            head1 = head1.next
            head2 = head2.next
    return res

node = Node([1, 3, 4, 7])
node1 = Node([2, 3, 5, 7, 9])
print(compare(node, node1))
