'''
题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"
和"12e+4.3"都不是。
'''

'''
思路一：利用float强转

7ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            return float(s)
        except:
            return 0

'''
思路二：正则表达式

28ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return 0
        import re
        # 正则表达式，*匹配前一个字符出现无限次或0次，？匹配前一个字符出现一次或0次，+匹配前一个字符出现1次
        # 或无限次，.表示小数点已经转义了
        return re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$', s)

'''
思路三：判断s中所有字符串，以e为界，e后面不能出现.或空，否则直接返回False，然后把e前后两部分全部放到
一个判断函数里面，考虑所有出现的字符串，+-不能出现在首位，字符串里面.出现次数不能超过1

28ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s or len(s) <= 0:
            return 0
        alist = [i.lower() for i in s]
        if 'e' in alist:
            index = alist.index('e')
            front = alist[:index]
            behind = alist[index + 1:]
            if '.' in behind or len(behind) == 0:
                return False
            isfront = self.Digit(front)
            isbehind = self.Digit(behind)
            return isfront and isbehind
        else:
            isNum = self.Digit(alist)
            return isNum

    def Digit(self, alist):
        dotNum = 0
        allowNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
        for i in range(len(alist)):
            if alist[i] not in allowNum:
                return False
            if alist[i] == '.':
                dotNum += 1
            if alist[i] in '+-' and i != 0:
                return False
        if dotNum > 1:
            return False
        return True

















