# while True:
#     try:
#         x = input()
#         res = []
#         for i in range(len(x)):
#             print(x[i])
#             if x[i].islower():
#                 print(x[i])
#                 if x[i] == 'z':
#                     x[i] = 'a'
#                 else:
#                     y1 = chr(ord(x[i]) + 1)
#                     # print(y)
#                 res.append(y1.upper())
#                 # print(res)
#             if x[i].isnumeric():
#                 if x[i] == '9':
#                     x[i] = '0'
#                 else:
#                     y2 = str(int(x[i]) + 1)
#                 res.append(y2)
#             if x[i].isupper():
#                 if x[i] == 'Z':
#                     x[i] = 'z'
#                 else:
#                     y3 = chr(ord(x[i]) - 1)
#                 res.append(y3.lower())
#         print(''.join(res))
#
#     except:
#         break

while True:
    try:
        a, b = input(), input()
        resA, resB = "", ""
        for i in a:
            if i.isupper():
                if i != "Z":
                    resA += chr(ord(i) + 1).lower()
                else:
                    resA += "a"
            elif i.islower():
                if i != "z":
                    resA += chr(ord(i) + 1).upper()
                else:
                    resA += "A"
            elif i.isdigit():
                if i != "9":
                    resA += chr(ord(i) + 1)
                else:
                    resA += "0"
        for i in b:
            if i.isupper():
                if i != "A":
                    resB += chr(ord(i) - 1).lower()
                else:
                    resB += "z"
            elif i.islower():
                if i != "a":
                    resB += chr(ord(i) - 1).upper()
                else:
                    resB += "Z"
            elif i.isdigit():
                if i != "0":
                    resB += chr(ord(i) - 1)
                else:
                    resB += "9"
        print(resA)
        print(resB)
    except:
        break
