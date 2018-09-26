# n, m = map(int, input().split())
#
# for i in range(n):
#     for j in range(i, n + 1):
#         if i + j == m:
#             print(i, j)

# dfs
n, m = list(map(int, input().split()))
li = []

def f(n, m, l, k):
    if m == 0:
        print(' '.join(l))
    for i in range(k, n + 1):
        if i > m:
            break
        l.append(str(i))
        f(n, m - i, l, i + 1)
        l.pop()

f(n, m, li, 1)
