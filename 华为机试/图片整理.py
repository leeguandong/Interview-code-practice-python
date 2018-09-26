while True:
    try:
        x = input()
        res = []
        res1 = []
        for i in x:
            res.append(ord(i))
        for j in sorted(res):
            res1.append(chr(j))
        print(''.join(res1))
    except:
        break
