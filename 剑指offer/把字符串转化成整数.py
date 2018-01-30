'''
题目：将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
'''

'''
思路一： 使用int(),但是通过了

29ms
5516k
'''

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        try:
            return int(s)
        except:
            return 0

'''
思路二：就是一些特殊处理，比如 +123，就不合理，123前面不需要+，但是-123就合理，因为这是个负数

27ms
5624k
'''

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        num = []
        numbers = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for i in s:
            if i in numbers.keys():
                num.append(numbers[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0
        ans = 0
        for i in num:
            ans = ans * 10 + i
        if s[0] == '-':
            ans = 0 - ans
        return ans

