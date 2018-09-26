x = input().split()
n1 = [int(i) for i in input().split()]
n2 = [int(i) for i in input().split()]

res = []
for i in range(len(n1)):
    res.append(n1[i] + n2[i] - 2)

print(min(res))
