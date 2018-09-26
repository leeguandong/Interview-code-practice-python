# while True:
# x = input().split()
# y = x[0].index('\\')
# print(y)
# count = x[y[-1]:]
# if count >= 16:
#     count = count[-16:]
# print(count)

error = dict()
filelist = []
while True:
    try:
        record = ''.join(''.join(input().split('\\')[-1].split()))
        filename = record.split()
        if len(filename[0]) >= 16:
            filename[0] = filename[0][-16:]
        record = ''.join(filename)
        if record not in error.keys():
            error[record] = 1
            filelist.append(record)
        else:
            error[record] += 1
    except:
        break
key = filelist[-8:]
for each in key:
    print(''.join(each.split()), error[each])
