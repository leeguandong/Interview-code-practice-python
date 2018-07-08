'''
题目：计算字符串最后一个单词的长度，单词以空格隔开。
'''

'''
思路：split() 空格为界，字符串转列表

38ms
3824k
'''

a = input().split()
if len(a) > 1:
    print(len(a[-1]))
else:
    print(len(a[0]))
