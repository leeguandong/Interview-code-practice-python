# while True:
#     try:
#         n = input()
#         start = 0
#         for i in range(n):
#             start += i
#             count = start
#             for j in range(i + 2, n + 2):
#                 print(count + 1)
#                 count += j
#
#     except:
#         break

def minusOne(num):
    return num - 1

while True:
    try:
        lineNum = int(input())
        temp = []
        for i in range(2, lineNum + 2):
            temp.append(sum(range(i)))
        for j in range(lineNum):
            print(' '.join(map(str, temp)))
            temp = list(map(minusOne, temp[1:]))
    except Exception:
        break
