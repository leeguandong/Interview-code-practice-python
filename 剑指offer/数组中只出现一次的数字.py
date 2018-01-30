'''
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

'''
思路一：利用python自带的counter库

27ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        from collections import Counter
        # 返回一个列表，map（f,input）,对input进行f操作，第一个参数lambda函数，意思取返回值中的第一个数，因为counter函数返回的是字典，
        # counter（）.most_common返回的是有序的计数字段，去最后两个，顺序是从大到小的。
        return list(map(lambda c:c[0],Counter(array).most_common()[-2:]))

'''
思路二：异或运算
'''

