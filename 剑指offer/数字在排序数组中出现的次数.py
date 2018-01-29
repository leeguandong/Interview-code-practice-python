'''
题目：统计一个数字在排序数组中出现的次数。
'''

'''
思路一：count函数是顺序查找，最坏时间复杂度是O(n)

27ms
5760k
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)

'''
思路二：看见有序就要想起使用二分法查找,最坏时间复杂度是O(logn)
'''





