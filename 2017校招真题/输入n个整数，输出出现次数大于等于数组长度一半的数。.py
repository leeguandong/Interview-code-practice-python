x = [int(i) for i in input().split()]
for i in x:
    k = x.count(i)
    if k * 2 >= len(x):
        print(i)
        break
