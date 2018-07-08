'''
题目：•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
     •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
'''

'''
思路：

37ms
3696k
'''

str1 = input()
str2 = input()

def out(str):
    a = len(str) % 8
    if a != 0:
        str = str + ('0' * (8 - a))
    for i in range(len(str) // 8):
        print(str[i * 8:8 * (i + 1)])

out(str1)
out(str2)
