# 每两个汽水瓶换一个，所以除以 2 就可以了

while True:
    try:
        a = int(input())
        if a != 0:
            print(a // 2)
    except:
        break
