# 这种题目一般都是动态规划或者贪心算法
# 当然可以暴力，我自己也只会暴力

x = int(input())

def getcount(x):
    for i in range(x // 6 + 1):
        if (x - i * 6) % 8 == 0:
            return i + (x - i * 6) // 8
    return -1

print(int(getcount(x)))
