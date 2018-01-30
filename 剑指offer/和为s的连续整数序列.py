'''
题目：小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,
21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
'''

'''
思路：设定两个指针，先分别指向数字1和数字2，并设这两个指针为small和big，对small和big求和，如果和大于目标值，
则从当前和中删除small值，并把small值加一，如果和小于目标值，则把big值加一，再把新的big值加入和中。如果和等于
目标值，就输出small到big的序列，同时把big加一并加入和中，继续之前的操作。

举例看起来更好理解一点，虽然是while循环里面没有做small到big之间的连接加减，但是由于都是从相邻出发，加和都是基于
1 2 3相邻数基础之上的加和，大了就对第一个数不断减，小了就对最后一个数不断加即可。
举例：  输入 tsum = 5
            1    2
            middle = 3   cursum = 3
            1 < 3:
                  3 < 5:
                       1     2    3
                       cursum = 1 + 2 + 3 = 6
                       6 > 5:
                            cursum - small = 6 - 1 = 5
                            return       2     3

30ms
5620k
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1) // 2
        cursum = big + small
        output = []

        while small < middle:
            if cursum == tsum:
                output.append(list(range(small, big + 1)))
            while cursum > tsum and small < middle:
                cursum -= small
                small += 1
                if cursum == tsum:
                    output.append(list(range(small, big + 1)))
            big += 1
            cursum += big
        return output
