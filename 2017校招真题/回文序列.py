X = int(input())
n = [int(i) for i in input().split()]

def huiwen(n, start, end):
    left = n[start]
    right = n[end]
    time = 0
    while start < end:
        if left < right:
            start += 1
            left += n[start]
            time += 1
        elif left > right:
            end -= 1
            right += n[right]
            time += 1
        elif left == right:
            start += 1
            end -= 1
            left = n[left]
            right = n[right]
    return time

print(huiwen(n, 0, X - 1))
