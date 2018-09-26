# x = input().split()
#
# res = []
# no = []
# for i in x:
#     no = i[::-1]
#     # 321 001
#     for j in range(len(no)):
#         if no[j] != '0':
#             no = no[j:]
#             break
#     # print(no)
#     res.append(no)
# n = str(int(res[0]) + int(res[1]))
# print(n)
# n = n[::-1]
# for j in range(len(n)):
#     if n[j] != '0':
#         n = n[j:]
#         break
# print(n)

# 731 288

a = input().split()
print(int(str(int(a[0][::-1]) + int(a[1][::-1]))[::-1]))