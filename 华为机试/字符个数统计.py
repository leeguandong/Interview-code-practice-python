result = ''

for i in input():
    if i not in result:
        result += i
print(len(result))
