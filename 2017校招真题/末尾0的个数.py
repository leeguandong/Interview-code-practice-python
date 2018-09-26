x = int(input())

n = 1
for i in range(1, x + 1):
    n *= i
n = str(n)[::-1]
count = 0
for i in n:
    if i != '0':
        break
    count += 1
print(count)
