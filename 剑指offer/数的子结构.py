'''
题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

'''
分析，两个序列才能确定一个一棵树，所以先用先序遍历，再用字符串进行匹配是不对的，因为的树的结构你确定不了。
这一题，首先判断根节点是不是相同，不相同是一个递归，把pRoot1的左右子树一次和PRoot2进行判断
如果根节点相同，那么进入下一个函数，接着判断，左边节点的下一级和左边子树下一级是不是相同，又是一个递归。
两个递归操作
29ms
5632k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        # 判断根节点
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.same(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def same(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        # 这一步不断判断下一个节点，因为是递归操作。
        if pRoot1.val != pRoot2.val:
            return False
        return self.same(pRoot1.left, pRoot2.left) and self.same(pRoot1.right, pRoot2.right)
