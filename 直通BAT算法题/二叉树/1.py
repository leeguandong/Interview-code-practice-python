# x = input().split()
# y = input().split()
# z = input().split()
#
# res = []
# for i in x:
#     for j in y:
#         for k in z:
#             n = i.replace(j, k)
#             res.append(n)
#
# print(" ".join(res))

# res = []
# x = input()
# for i in range(len(x)-1):
#     # print(i)
#     if int(x[i]) % 3 == 0 or int(x[i]) == 0:
#         res.append(x[i])
#     elif int(x[i] + x[i + 1]) % 3 == 0:
#         res.append(x[i] + x[i + 1])
# print(len(res))

# x = input()
# y = input()
# y = set(y)
# y = list(y)
# m = (int(y[0]) * int((x[0] + x[1]))) / int(x[0])
# print("%.2f" % m)

x = input()
res1 = []
m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(x)):
    if x[i] == 0:
        res1.append(i)
for i in res1:
    for j in range(len(m)):
        if j == i:
            m.remove(m[j])
print(m)