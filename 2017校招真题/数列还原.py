'''
思路：将 A 中缺失的部分补齐，然后求顺序对数，等于 k 则计数+1.
为此，先找到 A 缺失的是哪些数字，它们分别在什么位置。
其次，将这些缺失的数字全排列，分别按位置填充到 A 中，
计算当前组合的情况下 A 的顺序对数。

## 全排列：从 n 个不同元素中任取 m 个元素，按照一定的顺序排列起来，
叫做从 n 个不同元素中取出 m 个元素的一个排列。当 m=n 时所有的排
列情况叫做全排列。
'''

from itertools import permutations

# 求 A 中顺序对数
def number(A):
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] < A[j]:
                count += 1
    return count

n, k = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
B = list(range(1, n + 1))
X = list(set(B).difference(set(A)))  # B 和 A 的差集，即缺失的数字
Y = list(permutations(X))  # 求 X 的全排列
index = []
for i in range(n):
    if A[i] == 0:
        index.append(i)  # A 中0所在的位置的索引
m = len(index)
count = 0

# 往队列中嵌入全排列
for x in Y:
    for i in range(m):
        A[index[i]] = x[i]
    num = number(A)
    if num == k:
        count += 1
print(count)
