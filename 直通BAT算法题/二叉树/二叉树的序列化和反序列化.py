# 先序
class Tree():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if not root:
        return '#!'
    res = root.val + ['!']
    res += preorder(root.left)
    res += preorder(root.right)
    return res

tree = Tree([1])
print(preorder(tree))

# 反序列化(先序)
def recoByPreString(prestr):
    def reconpreorder(values):
        key = values.pop(0)
        if key == "#":
            return None
        root = Tree(key)
        root.left = reconpreorder(values)
        root.right = reconpreorder(values)
        return root

    values = prestr.split('!')
    return reconpreorder(values)
