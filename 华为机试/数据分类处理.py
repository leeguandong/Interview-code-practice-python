while True:
    try:
        a = input().split()[1:]
        b = map(str, sorted(map(int, set(input().split()[1:]))))
        totalNum = 0
        res = ''
        for num in b:
            singleRes, count = '', 0
            for i, v in enumerate(a):
                if num in v:
                    singleRes += str(i) + '' + ''
                    totalNum += 2
                    count += 1
            if count:
                singleRes = num + '' + str(count) + '' + singleRes
                totalNum += 2
            res += singleRes
        print((str(totalNum) + '' + res).rstrip())
    except:
        break
