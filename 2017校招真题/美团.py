# x = int(input())
# res = []
# for i in range(x - 1):
#     res.append(input().split())
# # print(res)
#
# for i in range(1, len(res)):
#     if res[i - 1][1] == res[i][0]:
#         x -= 1
# print(x + 1)


k, d = map(int, input().split())
l = input().split()

res = []
for i in range(len(l)):
    if l[i] == '0' and l[i + 1] == '1':
        res.append(l[i])
        res.append(l[i + 1])

# print(res)
if res[:-1] == '1':
    for i in range(d):
        res[:(-2 - 2 * i)] = '1'

print(res.count(1))
