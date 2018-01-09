'''
题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印
'''

'''
广度优先层次遍历，利用一个队列来实现
层序遍历的基本过程是：
先根节点入队，然后：
1.从队列中取出一个元素
2.访问该元素所指的结点
3.若该元素所指结点的左、右孩子结点非空，则将其左、右孩子的指针顺序入队

利用队列，首先将根节点放入队列中，取队列的首节点，把值存进列表，然后考虑左右指针，把指针放进列表，在存值

33ms
5900k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = []
        result = []

        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result