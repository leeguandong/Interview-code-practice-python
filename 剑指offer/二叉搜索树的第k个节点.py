'''
题目：给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序
第三个结点的值为4。
'''

'''
思路：二叉搜索树按照中序遍历的顺序打印出来正好就是排序好的顺序。
     所以，按照中序遍历顺序找到第k个结点就是结果。

28ms
5632k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global result
        result = []
        middle = self.midorder(pRoot)
        if k <= 0 or len(middle) < k:
            return None
        else:
            return middle[k - 1]

    def midorder(self, pRoot):
        if not pRoot:
            return []
        self.midorder(pRoot.left)
        result.append(pRoot)
        self.midorder(pRoot.right)
        return result