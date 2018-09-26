# x1 = raw_input()
# x2 = raw_input()
#
# count = 0
# for i in range(len(x1)):
#     for j in range(i, len(x2)):
#         if x1[i] == x2[j]:
#             continue
#         else:
#             count += 1
#
# if int(len(x1[0])) - count <= 1:
#     print 1
# else:
#     print 0


x1 = raw_input()
x2 = raw_input().split()

res = []
j = 0
k = 0
for i in range(3):
    if i == 0:
        res.append(x2[0])
        continue
    if i % 2 != 0:
        x3 = list(x2)
        while x3:
            if j > len(x2):
                break
            res.append(x2[j])
            j += 2
            x3.pop()
    if i % 2 == 0:
        x4 = list(x2)
        while x4:
            if j > len(x2):
                break
            res.append(x2[k])
            k += 2
            x4.pop()

print res
print sum(int(i) for i in res) - 1

