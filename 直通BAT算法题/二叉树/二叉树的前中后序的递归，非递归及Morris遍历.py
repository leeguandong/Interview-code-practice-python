class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# def create_tree(root):
#     element = input("Enter a key: ")
#     if element == '#':
#         root = None
#     else:
#         root = TreeNode(element)
#         print(root)
#         root.left = create_tree(root.left)
#         print(1)
#         root.right = create_tree(root.right)
#         print(2)
#     return root
#
# print(create_tree([None]))

class Tree():
    def __init__(self):
        self.root = None

    def add(self, item):
        node = TreeNode(item)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur = queue.pop(0)
            if cur.left == None:
                cur.left = node
                return
            else:
                queue.append(cur.left)

            if cur.right == None:
                cur.right = node
                return
            else:
                queue.append(cur.right)

    # 广度遍历
    def breadth_travel(self):
        if self.root == None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.val, end='')
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)

    # 深度遍历
    # 先序
    def preorder(self, node):
        if node == None:
            return
        print(node.val, end='')
        self.preorder(node.left)
        self.preorder(node.right)

    # 中序
    def middleorder(self, node):
        if node == None:
            return
        self.middleorder(node.left)
        print(node.val, end='')
        self.middleorder(node.right)

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.right)
        self.postorder(node.left)
        print(node.val, end='')

if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    tree.preorder(tree.root)
    tree.middleorder(tree.root)
    tree.postorder(tree.root)
