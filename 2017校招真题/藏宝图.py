# 体会一下，真的很好， 贪心
x = input()
y = input()

for i in x:
    if y and i==y[0]:
        y =y[1:]
print('No' if y else 'Yes')
