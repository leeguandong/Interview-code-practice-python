# k, d = map(int, input().split())
# arr = [int(i) for i in input().split()]
#
# class sum1():
#     def __init__(self):
#         self.count = 0
#
# def subset(self, arr, i, d):
#     if d == 0:
#         self.count += 1
#         return self.count
#     elif arr[0] == d:
#         self.count += 1
#         return self.count
#     elif arr[i] > d:
#         return subset(self, arr, i - 1, d)
#     else:
#         A = subset(self, arr, i - 1, d)
#         B = subset(self, arr, i - 1, d - arr[i])
#         return A or B
#
# no = sum1()
# subset(no, arr, k, d)

# 递归关系式
# dp[i][j] = dp[i-1][j] + dp[i-1][j-A[i]]
# i表示数组下标，j表示前i个元素的和，dp[i][j]表示前i个元素和为j的方案数
n, m = map(int, input().split())
a = map(int, input().split())

dp = [0 for i in range(m + 1)]
dp[0] = 1

for i in range(n):
    j = m
    while j >= a[i]:
        dp[j] += dp[j - a[i]]
        j -= 1
print(dp[m])

