x = int(input())
y = int(x ** 0.5)

count = 0
for i in range(0, y + 1):
    for j in range(0, y + 1):
        if i ** 2 + j ** 2 == x:
            if i == 0 and j == 0:
                count += 1
            if i == 0 or j == 0:
                count += 2
            if i != 0 and j != 0:
                count += 4

print(count)
