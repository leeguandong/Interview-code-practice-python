# 将所有的节点放置到一个数组中，对这个数组进行partition调整（快排调整过程），再将每个数组中每个节点串起来即可。
# 快排-递归

def list(head, pivot):
    def partition(nodeArr, pivot):
        left = - 1
        right = len(nodeArr)
        index = 0
        while index < right:
            if nodeArr[index].val < pivot:
                left += 1
                nodeArr[left], nodeArr[index] = nodeArr[index], nodeArr[left]
                index += 1
            elif nodeArr[index].val == pivot:
                index += 1
            else:
                right -= 1
                nodeArr[index], nodeArr[right] = nodeArr[right], nodeArr[index]

    if head == None or head.next == None:
        return head
    cur = head
    n = 0
    while cur != None:
        n += 1
        cur = cur.next
    nodeArr = []
    cur = head
    while cur != None:
        nodeArr.append(cur)
        cur = cur.next
    partition(nodeArr, pivot)
    for i in range(n - 1):
        nodeArr[i].next = nodeArr[i + 1]
    nodeArr[-1].next = None
    return nodeArr[0]
