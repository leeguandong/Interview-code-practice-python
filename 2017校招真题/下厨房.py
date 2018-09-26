# 第一个问题就是输入的问题，没说输入多少行
# 第二个问题就是去掉重复字符的问题

x = []
while True:
    try:
        m = input().split()
        x.extend(m)
    except:
        print(len(set(x)))
        break
