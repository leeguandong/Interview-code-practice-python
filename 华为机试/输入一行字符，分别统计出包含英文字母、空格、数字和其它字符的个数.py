while True:
    try:
        x = input()

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in x:
            if i.isalpha():
                count1 += 1
            elif i.isspace():
                count2 += 1
            elif i.isnumeric():
                count3 += 1
            else:
                count4 += 1
        print(count1)
        print(count2)
        print(count3)
        print(count4)
    except:
        break
