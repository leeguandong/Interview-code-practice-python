while True:
    try:
        x = input()
        n = input().split()

        res = []
        res1 = []
        Cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V',
               'W', 'X', 'Y', 'Z']
        for i in x:
            if i not in res:
                res.append(i)
            else:
                continue
        for i in res:
            res1.append(i.upper())

        res2 = []
        for i in Cap:
            if i not in res1:
                res2.append(i)
            else:
                continue

        res3 = []
        newres = res1 + res2
        # print(newres)

        for i in ''.join(n):
            if i.isupper():
                if i in Cap:
                    res3.append(newres[Cap.index(i)])
            if i.islower():
                if i.upper() in Cap:
                    res3.append(newres[Cap.index(i.upper())].lower())

        print(''.join(res3))
    except:
        break
