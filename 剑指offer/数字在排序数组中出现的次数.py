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

对于一个有序数组，要考虑 1,2,2,2,3,4这种情况，计算k=2在数组中出现的次数，用二分法去找这个数，一个找最前面
出现的2的下标，一个找最后面2出现的小标，这样前后相减+1即可的到结果。

29ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            First = self.GetFirst(data, length, k, 0, length - 1)
            Last = self.GetLast(data, length, k, 0, length - 1)
            if First > -1:
                number = Last - First + 1
        return number

    def GetFirst(self, data, length, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            if middle > 0 and data[middle - 1] == k:
                end = middle - 1
            else:
                return middle
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1
        return self.GetFirst(data, length, k, start, end)

    def GetLast(self, data, length, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            if middle < end and data[middle + 1] == k:
                start = middle + 1
            else:
                return middle
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1
        return self.GetLast(data, length, k, start, end)
