# x = input()
#
# res = []
# for i in x:
#     if x.count(i) > 1:
#         res.append(i)
#
# print(''.join(res))

from collections import defaultdict
while True:
    try:
        a = input()
        dd = defaultdict(int)
        for i in a:
            dd[i] += 1
        for i in dd:
            if dd[i] == min(dd.values()):
                a = a.replace(i,'')
        print(a)
    except:
        break

