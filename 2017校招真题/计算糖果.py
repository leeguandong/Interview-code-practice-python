n = int(input())
x = [int(i) for i in input().split()]

sum = 0
max = x[0]
for i in range(n):
    if sum >= 0:
        sum += x[i]
    else:
        sum = x[i]
    if sum > max:
        max = sum
print(max)
