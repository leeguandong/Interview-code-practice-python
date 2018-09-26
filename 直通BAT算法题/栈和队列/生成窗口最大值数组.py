# 双端队列
# 队列存的是数组的下标

def getwindows(arr, w):
    deque = []
    res = []

    for i in range(len(arr)):
        while deque and arr[deque[-1]] <= arr[i]:
            deque.pop()
        deque.append(i)
        if deque[0] <= i - w:
            deque.pop(0)
        if i - w + 1 >= 0:
            res.append(arr[deque[0]])
    return res

print(getwindows([4, 3, 5, 4, 3, 3, 6, 7], 3))
