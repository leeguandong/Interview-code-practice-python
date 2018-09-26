'''
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时
加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多
种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的
有效密码串吗？
'''
# x = input().split()
#
# def longest(x):
#     maximum = ''
#     temp = ''
#     for index in range(len(x)):
#         if len(maximum) >= len(x) - index:
#             break
#         for index2 in range(index + len(maximum), len(x) + 1):
#             fw = x[index:index2]
#             bw = fw[::-1]
#             if len(temp) > len(maximum):
#                 maximum = temp
#     return maximum
#
# print(longest(x))


'''
动态规划
             true                              j=i
dp[j][i] =   str[i] == str[j]                  i-j=1
             str[i] == str[j] && dp[j+1][i-1]  i-j>1
'''

def longestpalindrome(s):
    if s == s[::-1]:
        return len(s)
    maxlen = 0
    for i in range(len(s)):
        if i - maxlen >= 1 and s[i - maxlen - 1:i + 1] == s[i - maxlen - 1:i + 1][::-1]:
            maxlen += 2
            print(s[i - maxlen - 1:i + 1], maxlen)
            continue
        if i - maxlen >= 0 and s[i - maxlen:i + 1] == s[i - maxlen:i + 1][::-1]:
            maxlen += 1
            print(s[i - maxlen - 1:i + 1], maxlen)
        return maxlen

while True:
    try:
        a = input()
        if a:
            print(longestpalindrome(a))
    except:
        break
