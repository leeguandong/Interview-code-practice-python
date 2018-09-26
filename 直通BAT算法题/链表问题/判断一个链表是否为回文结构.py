def huiwen(arr):
    if arr == None or len(arr) < 2:
        return arr
    stack = []
    cur = arr
    while cur != None:
        stack.append(cur.val)
        cur = cur.next
    while stack:
        if stack.pop().val != arr.val:
            return False
        arr = arr.next
    return True
