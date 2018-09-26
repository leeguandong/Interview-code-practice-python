# x = int(input())
#
# def sum(i):
#     if i % 2 != 0:
#         return i
#     elif i % 2 == 0:
#         return sum(i / 2)
#
# n = 0
# for i in range(1, x + 1):
#     n += sum(i)
# print(int(n))

x = int(input())

def getsum(n):
    if n == 1:
        return 1
    return n*n/4 + getsum(n/2) if n%2==0 else n + getsum(n-1)

print(str(getsum(x)))
