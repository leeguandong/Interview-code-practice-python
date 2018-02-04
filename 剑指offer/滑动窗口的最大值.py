'''
题目：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及
滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的
滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''

'''
思路一：
      2 3 4   4   第一轮判断
      3 4 2   4
      4 2 6   6   第一轮结束时进入第二个判断条件
      2 6 2   6
      6 2 5   6
      2 5 1   5

23ms
5728k
'''

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0 or len(num) < size:
            return []
        length = len(num)
        curnum = max(num[:size])
        ans = [curnum]
        # 循环次数是length-size，是因为滑窗大小是size，length只能有length-size个滑窗
        for i in range(0, length - size):
            # 对滑窗内每个数字都进行扫描，直到找到和最大值相等数字，相等表明我的一个滑窗扫描结束，进入下一个滑窗进行扫描，并取最大值
            if num[i] == curnum:
                curnum = max(num[i + 1:i + 1 + size])
            # 跳过一个滑窗字符为首的一个滑窗，进入一个新的判断滑窗
            elif num[i + size] > curnum:
                curnum = num[i + size]
            ans.append(curnum)
        return ans

'''
思路二：用双向队列做，没看懂


'''

