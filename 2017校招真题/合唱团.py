'''
题目要求是 n 个学生中选择 k 个，使这 k 个学生的能力值乘积最大，这是一个最优化问题，在优化过程中，提出了相邻
两个学生的位置编号差不超过 d 的约束。

递归或者动态变化
1.对该问题的分解是关键
从 n 个学生中，选择 k 个，可以看成是：先从 n 个学生里选择最后1个，然后在剩下的里选择 k-1 个，并且让这1个和
前一个满足约束条件
2.数学描述
记第 k 个人的位置为1，则可以用f[1][k]表示从 n 个人中选择 k 个的方案。
然后它的子问题，需要从1前面的left个人里面，选择 k-1 个，这里left表示
k-1 个人中最后一个(即第k-1个)人的位置，因此，子问题可以表示成f[left][k-1]

在n和k定了之后，需要求解出n个学生选择k个能力乘积的最大值。因为能力值有正
有负，所以
当1对应的学生能力值为正时
f[1][k] = max{f[left][k-1] arr[i]}(min{k-1,1-d}<=left<=1-1)

'''

x1 = int(input())
x2 = [int(i) for i in input().split()]
k, d = map(int, input().split())

fmax = [[0 for i in range(x1)] for i in range(k)]
print(fmax)
fmin = [[0 for i in range(x1)] for i in range(k)]

for kk in range(k):
    for i in range(x1):
        if kk == 0 or i == 0:
            fmax[kk][i] = x2[i]
            fmin[kk][i] = x2[i]
        else:
            M = []
            for t in range(max(i - d, 0), i):
                M.extend([fmax[kk - 1][t] * x2[i], fmin[kk - 1][t] * x2[i]])
            fmax[kk][i], fmin[kk][i] = max(M), min(M)
print(max(fmax[k - 1]))
