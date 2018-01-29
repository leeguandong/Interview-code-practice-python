'''
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

'''
将输入数组转成字符串，利用cmp比较mn或者nm的大小，进行从小到大的排序

notes:
31ms
5596k
'''

import operator

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = list(map(str, numbers))
        # 在python3.x中已经没有cmp函数，要是用operator函数进行比较，cmp函数就是比较输入两个字符串之间大小的数字
        # cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
        # 是两两对象之间的比较，排序默认是从小到大，在这个函数内部实现的两两排序
        numbers.sort(cmp=lambda x, y: operator.eq(x + y, y + x))
        if numbers[0] == '0':
            return 0
        else:
            # ''.join实现了字符串之间的连接
            return ''.join(numbers)
