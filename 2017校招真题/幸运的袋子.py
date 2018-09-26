# x = input()
# y = map(int,input().split())
# n = 0
# m = 1
# count = 0
# for i in y:
#     n += i
#     m *= i
#     print(n,m)
#     if m < n:
#         count +=1
#
# print(count)

'''
这个问题是求有重复数字的集合的所有子集的一个扩展
加了限制条件，这些限制条件恰好可以用来剪枝

深度优先搜索 + 剪枝
'''
n = int(input())
x = sorted(list(map(int, input().split())))  # 从小到大排序

# s 为和，p 为积，pos 为初始位置
def dfs(x, pos, s, p):
    ans = 0
    i = pos
    while i < n:
        if s + x[i] > p * x[i]:
            ans += 1 + dfs(x, i + 1, s + x[i], p * x[i])
        # 第一个测试案例中 1 1 1 就有问题，后面的等于前面的，会存在重复递归的问题
        elif x[i] == 1:
            ans += dfs(x, i + 1, s + 1, p)
        else:
            break
        while i < n - 1 and x[i] == x[i + 1]:
            i += 1
        i += 1
    return ans

print(dfs(x, 0, 0, 1))
