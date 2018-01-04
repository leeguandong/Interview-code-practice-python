'''
题目：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

'''
第三位是前两位之和，一直迭代的
25ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0,1]
        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return res[n]