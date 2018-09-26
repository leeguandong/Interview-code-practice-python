'''
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？

'''

while True:
    try:
        x = [int(i) for i in input().split()]

        res = [1, 2]

        for i in range(x[0] - 3):
            res.append(res[-1] + res[-2])

        # print(res)
        print(res[-1])
    except:
        break
