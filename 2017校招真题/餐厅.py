# 在 m 批客人中选择 n 批上 n 个桌子
n, m = [int(x) for x in input().split()]
# 每个桌子可容纳的最大人数
table = [int(x) for x in input().split()]
# 分别表示第 i 批客人的人数和预计消费金额
cus = [[int(x) for x in input().split()] for i in range(m)]

# 将桌子按可容纳人数从小到大排列
table.sort()
# 按每批顾客的人数从小到大排序
cus = sorted(cus, key=lambda x: x[0])
# 总金额
money = 0

for i in range(n):
    # 盛放第 i 个可接受的顾客批 j
    temp = []
    # 注意 range 中要用 cus 的 length 时更新
    for j in range(len(cus)):
        if cus[j][0] > table[i]:
            break
        temp.append(cus[j])
    # 按消费金额排序
    temp = sorted(temp, key=lambda x: x[1])
    if temp:
        money += temp[-1][1]
        # 此批客人已就坐
        cus.remove()
print(money)
