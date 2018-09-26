x = input().split()
k = ''.join(list(map(str, input().split())))
# k = x[-1]
# x.remove(x[-1])

res = []
for i in x:
    for j in i:
        if j in k:
            # i.replace(j, '')
            # print(i)
            n = i.index(j)
            i = i[:n] + i[n + 1:]
    res.append(i)

print(' '.join(list(map(str, res))))
