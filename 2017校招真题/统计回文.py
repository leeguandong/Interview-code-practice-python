n1 = input()
n2 = input()
n = []

def huiwen(s):
    return s == s[::-1]

count = 0
for i in range(len(n1) + 1):
    n = n1[:i] + n2 + n1[i:]
    if huiwen(n):
        count += 1
print(count)
