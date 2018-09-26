'''
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复
说明:长度超过2的子串
'''

# import re, sys
#
# for i in sys.stdin.readlines():
#     print("OK" if len(i.strip()) > 8 and sum(
#         [1 if re.search(r"[A-Z]", i.strip()) else 0, 1 if re.search(r"[a-z]", i.strip()) else 0,
#          1 if re.search(r"[0-9]", i.strip()) else 0, 1 if re.search(r"[^0-9a-zA-Z]", i.strip()) else 0]) > 2 and sum(
#         map(lambda c: i.strip().count(i.strip()[c:c + 3]) > 1, range(1, len(i.strip()) - 3))) == 0 else "NG")

# 略微思考会发现，只需要判断长度为3的子串是否出现即可。因为假设子串长度为4的出现，则一定包括了长度为3的子串。同时需要注意，
# 本题说的子串指包括了部分子串重叠的情况，
# 例如Qw11111*ed这个是不能通过的。再就是需要注意，判断子串的时候只需要判断到len(str)-3就行了。

import sys

try:
    # 大小写，字母，
    def panchar(sss):
        standard = [0] * 4
        for i in sss:
            # print(i)
            # 0
            # 2
            # 1
            # A
            # b
            # print(len(sss))
            # 数字
            if i.isdigit():
                standard[0] = 1
                # print(i.isdigit())
            # 小写
            if i.islower():
                standard[1] = 1
            # 大写
            if i.isupper():
                standard[2] = 1
            # 全都是字母，数字，空格
            if not i.isalpha() and not i.isdigit() and not i.isspace():
                standard[3] = 1
            if sum(standard) >= 3:
                return False
        return True

    # 不能有相同长度超 2 的字串重复
    def zichuan(sss):
        for i in range(len(sss) - 3):
            zichuan_1 = sss[i: i + 3]
            zichuan_2 = sss[i + 1::]
            if zichuan_1 in zichuan_2:
                return True
        return False

    result = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        if len(line) <= 8:
            result.append('NG')
        # 大小写字母.数字.其它符号
        elif panchar(line):
            result.append('NG')
        elif zichuan(line):
            result.append('NG')
        else:
            result.append('OK')
    for i in result:
        print(i)
except:
    pass


# # 循环输入，try catch
# while True:
#     try:
#         x = input().split()
#
#
#     except:
#         pass
