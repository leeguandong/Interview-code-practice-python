'''
题目：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、
10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出
任意非负整数区间中1出现的次数。
'''

'''
思路1：例：对于824883294，先求0－800000000之间（不包括800000000）的，再求0－24883294之间的。
如果等于1，如1244444，先求0－1000000之间，再求1000000－1244444，那么只需要加上244444＋1，再求0－244444
之间的1如果大于1，例：0－800000000之间1的个数为8个100000000的1的个数加上100000000，因为从1000000000－
200000000共有1000000000个数且最高位都为1。对于最后一位数，如果大于1，直接加上1即可。

思路2：将1-n全部转换为字符串，只需要统计每个字符串中'1'出现的次数并相加即可
47ms
5504k
'''

def countDigitOne(self, n):
    result = 0
    if n < 0:
        return 0
        length = len(str(n))
        listN = list(str(n))
    for i, v in enumerate(listN):
        a = length - i - 1  # a为10的幂
        if i == length - 1 and int(v) >= 1:
            result += 1
            break
        if int(v) > 1:
            result += int(10 ** a * a / 10) * int(v) + 10 ** a
            if int(v) == 1:
                result += (int(10 ** a * a / 10) + int("".join(listN[i + 1:])) + 1)
    return result

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1,n+1):
            for i in str(i):
                if i == '1':
                    count += 1
        return count
