x = input().split()
length = len(x)

res = []
y = []
for i in range(length):
    y += str(x[i])
length1 = len(y)

y = y + y
# print(y)

for i in range(length1):
    # print(y[i:(i + length1)])
    if y[i:i + length1] not in res:
        res.append(y[i:i + length1])
    else:
        continue

print(res)
print(len(res))
