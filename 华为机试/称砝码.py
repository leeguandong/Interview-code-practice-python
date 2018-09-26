def fama(n, weight, nums):
    res = set()
    for i in range(nums[0] + 1):
        res.add(i * weight[0])
    for i in range(1, n):
        tmp = list(res)
        for j in range(1, nums[i] + 1):
            for wt in tmp:
                res.add(wt + j * weight[i])
    return len(res)

while True:
    try:
        n = int(input())
        weight = [int(i) for i in input().split()]
        nums = [int(i) for i in input().split()]
        print(fama(n, weight, nums))
    except:
        break

