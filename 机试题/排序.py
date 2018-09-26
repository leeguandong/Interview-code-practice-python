# https://blog.csdn.net/u012193416/article/details/78790448
# # 冒泡排序
# # 时间复杂度  O(n**2) 空间复杂度  O(1)
# x = [int(i) for i in input().split(',')]
#
# # print(x)
#
# def mpsort(x):
#     n = len(x)
#     # print(n)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             # print(x[j])
#             if x[j] > x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
# print(mpsort(x))

# # 选择排序
# # 时间复杂度 O(n**2) 空间复杂度  O(1)
# x = [int(i) for i in input().split(',')]
#
# def xzsort(x):
#     n = len(x)
#     for i in range(n - 1):
#         min = i
#         for j in range(i + 1, n):
#             if x[j] < x[min]:
#                 min = j
#         x[i], x[min] = x[min], x[i]
#     return x
#
# print(xzsort(x))

# # 插入排序
# # 时间复杂度 O(n**2) 空间复杂度  O(1)
# x = [int(i) for i in input().split(',')]
#
# def crsort(x):
#     n = len(x)
#     for i in range(1, n):
#         j = i
#         while j > 0:
#             if x[j] < x[j - 1]:
#                 x[j], x[j - 1] = x[j - 1], x[j]
#                 j -= 1
#             else:
#                 break
#     return x
#
# print(crsort(x))

# # 希尔排序
# # 时间复杂度 O(nlogn)-O(n**2) 空间复杂度  O(1)
# x = [int(i) for i in input().split(',')]
#
# def shellsort(x):
#     n = len(x)
#     gap = n // 2
#
#     while gap > 0:
#         for i in range(gap, n):
#             j = i
#             while j > 0:
#                 if x[j] < x[j - gap]:
#                     x[j], x[j - gap] = x[j - gap], x[j]
#                     j -= gap
#                 else:
#                     break
#         gap //= 2
#     return x
#
# print(shellsort(x))

# # 快速排序
# # 时间复杂度 O(nlogn) 空间复杂度  O(logn)-O(n)
# x = [int(i) for i in input().split(',')]
#
# def kpsort(x, first, last):
#     font = first
#     end = last
#     middle = x[first]
#
#     if first >= last:
#         return
#
#     while font < end:
#         while font < end and x[font] <= middle:
#             font += 1
#         x[end] = x[font]
#
#         while font < end and x[end] > middle:
#             end -= 1
#         x[font] = x[end]
#
#     x[font] = middle
#
#     kpsort(x, first, font - 1)
#     kpsort(x, font + 1, last)

# 归并排序
# 时间复杂度 O(nlogn)  空间复杂度  O(N)
x = [int(i) for i in input().split(',')]

def gbsort(x):
    length = len(x)
    if length <= 1:
        return x
    mid = length // 2

    left = gbsort(x[:mid])
    right = gbsort(x[mid:])

    left_point, right_pointer = 0, 0
    result = []

    while left_point < len(left) and right_pointer < len(right):
        if left[left_point] <= right[right_pointer]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right_pointer)
            right_pointer += 1

    result += left[left_point:]
    result += right[right_pointer]

    return result

print(gbsort(x))
