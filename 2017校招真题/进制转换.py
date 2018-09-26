# k, d = map(int, input().split())
#
# n = 0
# for i in range():
#     n += d ** i
#     if n == k:
#         print(i)
#     if n > k:
#         print(-1)

def baseN(num, b):
    res = ''
    if num > 0:
        while num:
            res = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ'[num % b] + res
            num = num // b
        return res
    else:
        num = -num
        while num:
            res = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ'[num % b] + res
            num = num // b
        return '-' + res

a, b = map(int, input().split())
print(baseN(a, b))
