n = [int(i) for i in input().split()]

arr, res = [], 0
for i in range(2, n[0] + 1):
    flag = True
    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            flag = False
            break
    if flag:
        arr.append(i)
# print(arr)

for i in range(len(arr)):
    if arr[i] > n[0] / 2:
        break
    else:
        if n[0] - arr[i] in arr:
            res += 1
print(res)
