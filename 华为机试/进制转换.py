'''
题目：写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）
'''

'''
思路一： 用 int(x,[base]) 将一个数字或 base 类型的字符串转换成整数。 缺省 base ，按十进制算

36ms
3448k
'''

while True:
    try:
        print(int(input(), 16))
    except:
        break

'''
思路二： 用 eval(source[, globals[, locals]]) ,将字符串转掉，变成一个数字，以十进制打印出来

35ms
3564k
'''

while True:
    try:
        n = input()
        n = eval(n)
        print(n)
    except:
        break
