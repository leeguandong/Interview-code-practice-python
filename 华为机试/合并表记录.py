'''
题目：数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，
     输出按照key值升序进行输出。
'''

'''
思路：


'''

n = input().split()
res = {}
for i in range(int(n[0])):
    k, d = map(int, input().split())
    if k in res.keys():
        res[k] = res[k] + d
    else:
        res[k] = d

for k, d in res.items():
    print(str(k) + ' ' + str(d))
