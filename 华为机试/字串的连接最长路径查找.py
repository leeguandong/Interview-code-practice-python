n = input().split()

res = []
print(int(n[0]))
for i in range(int(n[0])):
    res.append(input().split())

res.sort()
# print(res)

for i in res:
    print(''.join(i))
