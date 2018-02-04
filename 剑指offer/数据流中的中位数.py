'''
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''

'''
思路一：常规操作

29ms
5760k
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.array = []

    def Insert(self, num):
        # write code here
        self.array.append(num)
        self.array.sort()

    def GetMedian(self, M):
        # write code here
        length = len(self.array)
        if length % 2 == 1:
            return self.array[length // 2]
        return (self.array[length // 2] + self.array[length // 2 - 1]) / 2.0

'''
思路二：
为了保证插入新数据和取中位数的时间效率都高效，这里使用大顶堆+小顶堆的容器，并且满足：
1、两个堆中的数据数目差不能超过1，这样可以使中位数只会出现在两个堆的交接处；
2、大顶堆的所有数据都小于小顶堆，这样就满足了排序要求。

构建一个最大堆和一个最小堆，分别存储比中位数小的数和大的数。
当目前两堆总数为偶数的时候，把数字存入最大堆，然后重排最大堆，如果最大堆的堆顶数字大于最小堆堆顶数字，
则把两个堆顶数字交换，重排两堆，此时两堆数字总数为奇数，直接输出最大堆堆顶数字即为中位数；
如果当前两堆总数为奇数的时候，把数字存入最小堆，重排最小堆，如果最大堆的堆顶数字大于最小堆堆顶数字，
则把两个堆顶数字交换，重排两堆，此时两堆数字总数为偶数，取两堆堆顶数字做平均即为中位数

最大堆堆顶元素要小于最小堆堆顶的元素，最大堆，堆顶元素最大，从大到小，最小堆堆顶元素最小，从小到大，这样的话，
最大堆所有元素均小于最小堆了，中位数一定出现在两堆交替之间。

27ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def Insert(self, num):
        if self.count & 1 == 0:
            self.left.append(num)
        else:
            self.right.append(num)
        self.count += 1

    def GetMedian(self, x):
        if self.count == 1:
            return self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.count & 1 == 0:
            return (self.left[0] + self.right[0]) / 2.0
        else:
            return self.left[0]

    def MaxHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i;
            temp = alist[k];
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] < alist[index + 1]: index += 1
                if temp >= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

    def MinHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i;
            temp = alist[k];
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] > alist[index + 1]: index += 1
                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

