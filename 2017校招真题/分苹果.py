'''
1.先判断数组总和是否可以被n整除，否则没法分均匀。
2.然后再判断每个牛的苹果与平均值的差，若差不是2的倍数，也无法移动成功
3.如果前两个条件满足就把比均值多的苹果数减去均值，将其总数除以2，
就是得到的移动次数了。
'''

n = int(input())
ls = [int(i) for i in input().split()]

def splitapple(n, ls):
    if sum(ls) % n != 0:
        return -1
    count = 0
    avg = sum(ls) // n

    for i in ls:
        if (i - avg) % 2 != 0:
            return -1
        if i > avg:
            count += (i - avg)
    return (int(count // 2))

print(splitapple(n, ls))
