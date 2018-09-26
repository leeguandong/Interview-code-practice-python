'''
题目：功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
最后一个数后面也要有空格

详细描述：
函数接口说明：
public String getResult(long ulDataInput)
输入参数：
long ulDataInput：输入的正整数
返回值：
String

'''

'''
把输入的数进行因式分解，只不过分解的数必须是质数
思路：对于一个数来说，比如180，从2开始遍历，如果能被2整除，那么180/=2，并且输出2，之后再拿90重复上述操作
    直到变成1为止

45ms
3560k
'''

n, res = int(input()), []
for i in range(2, n // 2 + 1):
    while n % i == 0:
        res.append(i)
        n = n / i
print(" ".join(map(str, res)) + " " if res else str(n) + " ")
