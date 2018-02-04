'''
题目：请实现两个函数，分别用来序列化和反序列化二叉树
'''

'''
思路：最终要实现的是二叉树的序列化和反序列化。首先来看二叉树的序列化，二叉树的序列化就是采用前序遍历二叉树输出
节点，再碰到左子节点或者右子节点为None的时候输出一个特殊字符”#”。对于反序列化，就是针对输入的一个序列构建一棵
二叉树，我们可以设置一个指针先指向序列的最开始，然后把指针指向位置的数字转化为二叉树的结点，后移一个数字，继续
转化为左子树和右子树。当遇到当前指向的字符为特殊字符”#”或者指针超出了序列的长度，则返回None，指针后移，继续遍历。

26ms
5632k
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    flag = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.flag += 1
        l = s.split(',')
        # flag每次加1，从0开始，不能超过字符串长度，否则返回None
        if self.flag >= len(s):
            return None

        root = None
        # 新建一个树对象来反序列化字符串
        if l[self.flag] != '#':
            # 往树中存值,递归输入s没问题，因为l[self.flag]是不断往后取值的
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

