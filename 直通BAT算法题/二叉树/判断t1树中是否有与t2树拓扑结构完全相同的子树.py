class Tree():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def Top(t1, t2):
    def issubTosub(t1, t2):
        if not t1 and not t2:
            return True
        if t1.val != t2.val:
            return False
        return issubTosub(t1.left, t2.left) and issubTosub(t1.right, t2.right)

    if not t1 or not t2:
        return False
    return Top(t1, t2) or Top(t1.left, t2) or Top(t1.right, t2)
