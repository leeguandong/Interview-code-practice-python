# 每一棵树的父节点是他左边第一个比他大的数和他右边第一个比他大的数中较小的那个值
# 如果这个数是整个树中的最大值，那么他就作为整个数的头结点出现

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getMaxtree(self, arr):
        narr = [Node(arr[i]) for i in range(len(arr))]
        lBigMap = {}
        rBigMap = {}
        stack = []

        # 对输入的元素进行判断，输入元素大于栈顶元素，那么栈顶元素弹出直到小于输入元素
        for i in range(len(narr)):
            curNode = narr[i]
            while stack and stack[-1].value < curNode.value:
                cur = stack.pop()
                lBigMap[cur] = stack[-1] if stack else None
                rBigMap[cur] = curNode
            stack.append(curNode)

        # 上面的循环条件是两个，但是实际上最后还是会剩下来栈里面的几个元素
        while stack:
            cur = stack.pop()
            lBigMap[cur] = stack[-1] if stack else None
            rBigMap[cur] = None

        head = None
        for i in range(len(narr)):
            curNode = narr[i]
            left = lBigMap[curNode]
            right = rBigMap[curNode]
            if left == None and right == None:
                head = curNode
            elif left == None:
                if right.left == None:
                    right.left = curNode
                else:
                    right.right = curNode
            elif right == None:
                if left.left == None:
                    left.left = curNode
                else:
                    left.right = curNode
            else:
                parent = left if left.value < right.value else right
                if parent.left == None:
                    parent.left = curNode
                else:
                    parent.right = curNode
        return head

node = Node(None)
print(node.getMaxtree([3, 1, 2]))
