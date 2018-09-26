# 在于判断是不是数的这个isnumeric()函数
x = input()
curlen, curstr, maxlen, maxstr = 0, '', 0, ''

for i, v in enumerate(x):
    if v.isnumeric():
        curlen += 1
        curstr += v
        if curlen > maxlen:
            maxlen = curlen
            maxstr = curstr
    else:
        curlen = 0
        curstr = ''
print(maxstr)
