x, arr = input(), []

for i in range(int(x)):
    arr.append(input())

length, lex = sorted(arr, key=len), sorted(arr)

if length == arr and lex == arr:
    print('both')
elif length == arr:
    print('lengths')
elif lex == arr:
    print('lexicographically')
else:
    print('none')
