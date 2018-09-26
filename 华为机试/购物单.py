N_m = input().split()
N = int(N_m[0])
m = int(N_m[1])

v = []
p = []
q = []

for i in range(m):
    vpq = input().split()
    v.append(int(vpq[0]))
    p.append(int(vpq[1]))
    q.append(int(vpq[2]))

def max_fun(N, m, v, p, q):
    res = [[0] * (N - 1) for _ in range(m + 1)]
    # 商品
    for i in range(1, m + 1):
        # 价格
        for j in range(10, N + 1, 10):
            # 为主件时
            if q[i - 1] == 0:
                if v[i - 1] <= j:
                    res[i][j] = max(res[i - 1][j], res[i - 1][j - v[i - 1]] + v[i - 1] * p[i - 1])
            # 为配件时
            elif v[i - 1] + v[q[i - 1]] <= j:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - v[i - 1] - v[q[i - 1]]] + v[i - 1] * p[i - 1] + v[
                    q[i - 1] * p[q[i - 1]]])
    print(res[m][int(N / 10) * 10])

max_fun(N, m, v, p, q)

res[m]