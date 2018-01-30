'''
题目：汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后
的结果，即“XYZdefabc”。是不是很简单？OK，搞定它
'''

'''
思路一：

29ms
5760k
'''

# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:] + s[:n]

'''
思路二：对原字符串进行扩充两倍，在这个基础上直接从要反转的地方取就可以，相当于前n个字符串翻转了，思想非常好

28ms
5760k
'''

# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        length = len(s)
        s += s
        return s[n:length + n]

'''
尽量避免使用内置函数
思路三：首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后根据题目中给出的左旋转字符串的个数n，
用全字符串长度length减去旋转字符串个数n，求得对于新的字符串应该在哪一位进行旋转，然后分别旋转前[:length-n]子
串和[length-n:]子串，重新拼接两个子串即可。
举例：  n=2
       1 2 3 4 5
       5 4 3 2 1   整体反转
       3 4 5 1 2   对于5-2=3部分翻转，对于最后2 1再部分翻转

28ms
5760k
'''

# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s) < n or n < 0:
            return ''
        s = list(s)
        length = len(s)
        s = self.Reverse(s)
        s1 = self.Reverse(s[:length - n])
        s2 = self.Reverse(s[length - n:])
        result = ''.join(s1) + ''.join(s2)
        return result

    def Reverse(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s
