class Tree():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def printlayer(root):
    last = root
    queue = []
    queue.append(root)
    while queue:
        root = queue.pop(0)
        print(root.val, end='')
        if root.left:
            nlast = root.left
            queue.append(root.left)
        if root.right:
            nlast = root.right
            queue.append(root.right)
        if root == last and queue:
            last = nlast
