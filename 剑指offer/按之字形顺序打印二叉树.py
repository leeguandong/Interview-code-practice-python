'''
题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
'''

'''
思路一：按之字形顺序打印二叉树需要两个栈。我们在打印某一行节点时，拔下一层的子节点保存到相应的栈里。如果当前打印
的奇数层，则先保存左子节点再保存右子节点到第一个栈里；如果当前打印的是偶数层，则先保存右子节点再保存左子节点到
第二个栈里。

28ms
5512k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result,nodes = [],[pRoot]
        right = True
        # 处理思路很好的，有一个二级机制，通过nextStack存下一节点的，这节点里面的值通过=nodes再转移到curStack里面
        # 但是在nextStack中可以调整顺序的
        while nodes:
            nextStack,curStack = [],[]
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()
            right = not right
            result.append(curStack)
            nodes= nextStack
        return result

'''
思路二： 转换思路，存储的时候一直从左向右存储，打印的时候根据不同的层一次打印

25ms
5512k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        nodes,result,leftToright = [pRoot],[],True
        while nodes:
            curStack,nextStack = [],[]
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            # 调整的是一级的curStack的顺序了，不是二级的nextStack的顺序
            if not leftToright:
                curStack.reverse()
            if curStack:
                result.append(curStack)
            nodes = nextStack
            leftToright = not leftToright
        return result


