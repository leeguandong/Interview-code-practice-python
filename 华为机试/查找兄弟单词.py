'''
字典顺序：
两个单词(字母按照自左向右顺序)，先以第一个字母作为排序的基准，如果第一个字母相同，
就用第二个字母为基准，如果第二个字母相同就以第三个字母为基准。依次类推，如果
到某个字母不相同，字母顺序在前的那个单词顺序在前。如果短单词是长单词从首字母开始
连续的一部分，短单词顺序在前。
'''

# while True:
#     try:
#         x = input().split()
#         from collections import defaultdict
#
#         dd = defaultdict(list)
#         res = []
#
#         for i in range(1, int(x[0]) + 1):
#             # print(x[i])
#             dd[''.join(sorted(x[i]))].append(x[i])
#             # print(dd)
#         for key, value in dd.items():
#             if key == ''.join(sorted(x[-2])):
#                 res.append(value)
#                 # print(len(value) - 1)
#                 # print(value[int(x[-1])])
#
#         for i in res:
#             for j in i:
#                 if ''.join(j) == x[-2]:
#                     res[0].remove(j)
#
#         # print(res)
#         if res == []:
#             print(0)
#         else:
#             print(len(res[0]))
#             print(res[0][int(x[-1]) - 1])
#
#     except:
#         break


from collections import defaultdict

while True:
    try:
        dd = defaultdict(list)
        a = input().split()
        words, lookup, num, brothers = a[1:1 + int(a[0])], a[-2], int(a[-1]), []
        for i in words:
            dd[''.join(sorted(i))].append(i)
        for i in dd[''.join(sorted(lookup))]:
            if i != lookup:
                brothers.append(i)

        print(len(brothers))
        if brothers and num <= len(brothers):
            print(sorted(brothers)[num - 1])
    except:
        break
