while True:
    try:
        x = input().split(';')
        res = [0, 0]
        for i in range(len(x)):
            if x[i] == '':
                continue
            # print(x[i])
            # print(x[i][0])
            if x[i][0] == 'A':
                # print(''.join(x[i][1:]))
                if ''.join(x[i][1:]).isnumeric():
                    res[0] -= int(x[i][1:])
                    # print(res[0])
                else:
                    continue
            elif x[i][0] == 'D':
                if ''.join(x[i][1:]).isnumeric():
                    res[0] += int(x[i][1:])
                else:
                    continue
            elif x[i][0] == 'W':
                if ''.join(x[i][1:]).isnumeric():
                    res[1] += int(x[i][1:])
                else:
                    continue
            elif x[i][0] == 'S':
                if ''.join(x[i][1:]).isnumeric():
                    res[1] -= int(x[i][1:])
                else:
                    continue

        print(str(res[0]) + ',' + str(res[1]))
    except:
        break

