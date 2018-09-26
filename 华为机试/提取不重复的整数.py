result = ''

for i in input()[::-1]:
    if i not in result:
        result += i
print(result)
