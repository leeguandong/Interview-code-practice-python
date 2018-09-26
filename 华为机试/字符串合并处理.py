'''
将输入的两个字符串合并，要求是下标为奇数的字符和下标为偶数的字符分别从小到大
排序。
'''

while True:
    try:
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        # s是输入的合并后的字符串
        s = input().replace(' ', '')

        # ss为最终返回的字符串
        ss = ''

        # 字符串的奇数子串和偶数子串
        odd, even = '', ''
        # 经过下面的循环,提取奇数和偶数的子串
        for i, v in enumerate(s):
            if i % 2 == 0:
                even += v
            else:
                odd += v
        # 奇数与偶数部分排序
        odd = ''.join(sorted(odd))
        even = ''.join(sorted(even))

        # 如果字符串在0123456789abcdef范围内，对其做变换，否则不做任何处理
        for i in range(len(even)):
            if even[i] in '0123456789abcdefABCDEF':
                ss += dic[int(bin(dic.index(even[i].upper())).replace("0b", "").rjust(4, "0")[::-1], 2)]
            else:
                ss += even[i]
            # 注意偶数串可能比奇数串长一个字符，所以要判断一下
            if len(odd) != i:
                if len(odd) != i:
                    ss += dic[int(bin(dic.index(odd[i].upper())).replace('0b', '').rjust(4, '0')[::-1], 2)]
                else:
                    ss += odd[i]
        print(ss)
    except:
        break
