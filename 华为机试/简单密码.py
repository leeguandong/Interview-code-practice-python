x = input().split()

def mima(s):
    if s in 'Z':
        s = 'a'
    elif s.isupper():
        s = chr(ord(s.lower()) + 1)
    elif s in 'abc':
        s = '2'
    elif s in 'def':
        s = '3'
    elif s in 'ghi':
        s = '4'
    elif s in 'jkl':
        s = '5'
    elif s in 'mno':
        s = '6'
    elif s in 'pqrs':
        s = '7'
    elif s in 'tuv':
        s = '8'
    elif s in 'wxyz':
        s = '9'
    elif s in '0':
        s = '0'
    return s

res = []
for i in range(len(x[0])):
    res.append(mima(x[0][i]))

print(''.join(res))
