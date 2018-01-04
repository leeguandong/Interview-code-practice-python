'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

'''
方法一： 两个数组解
25ms
5504k
'''

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here

        res1 = []
        res2 = []
        for i in array:
            if i % 2 == 0:
                res1.append(i)
            else:
                res2.append(i)
        return res2 + res1

'''
方法二：类似冒泡的思想，相互交换
'''
