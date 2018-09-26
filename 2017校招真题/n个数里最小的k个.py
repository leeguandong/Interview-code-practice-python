x = [int(i) for i in input().split()]
k = x[-1]
x.remove(x[-1])
x.sort()
print(' '.join(list(map(str,x[:k]))))


# a = list(map(int, input().split()))
# lists, k = a[:-1], a[-1]
# print(" ".join(list(map(str, sorted(lists)[:k]))))