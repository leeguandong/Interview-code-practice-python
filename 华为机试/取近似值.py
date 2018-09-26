'''
题目：写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；
     小于5，则向下取整。
'''

'''
思路：

32ms
3436k
'''

try:
    while True:
        a = eval(input())
        if (a - int(a)) >= 0.5:
            print(int(a) + 1)
        else:
            print(int(a))
except:
    pass
