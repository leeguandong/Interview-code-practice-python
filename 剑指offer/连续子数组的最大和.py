'''
题目：HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常
需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望
旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他
忽悠住？(子向量的长度至少是1)
'''

'''
对于连续子数组，可以用一个数值来存储当前和，如果当前和小于零，那么在进行到下一个元素的时候，直接把当前和赋值为下
一个元素，如果当前和大于零，则累加下一个元素，同时用一个maxNum存储最大值并随时更新。也可以利用动态规划解决。

29ms
5624k
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array == None or len(array) <= 0:
            return 0

        sum = 0
        result = array[0]
        for i in range(len(array)):
            if sum <= 0:
                sum = array[i]
            else:
                sum += array[i]

            if sum > result:
                result = sum

        return result


