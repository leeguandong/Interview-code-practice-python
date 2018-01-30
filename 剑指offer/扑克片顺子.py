'''
题目：LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,
黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。为了方便起见,
你可以认为大小王是0。
'''

'''
思路：先统计王的数量，再把牌排序，如果后面一个数比前面一个数大于1以上，那么中间的差值就必须用王来补了。
看王的数量够不够，如果够就返回true，否则返回false。

31ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        zero = numbers.count(0)

        # 里面有numbers[i+1]操作，所以取不到最后一个数
        for i, v in enumerate(numbers[:-1]):
            if v != 0:
                # numbers中不能有两个相同的数字
                if numbers[i + 1] == v:
                    return False
                zero = zero - (numbers[i + 1] - v - 1)
                if zero < 0:
                    return False
        return True
