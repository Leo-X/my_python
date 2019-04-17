# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9

# 朴素的串匹配算法

# 从小到大升序
lst = [5, 4, 3, 1, 2, 0, 7, 8]


def insert_sort(arr):
    for i in range(1, len(arr)):
        a = arr[i]
        j = i
        while j > 0 and arr[j-1] > a:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


# insert_sort(lst)
# print('lst:', lst)


def select_sort(lst):
    for i in range(len(lst)-1):
        k = i
        for j in range(i, len(lst)):
            if lst[j] < lst[k]:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]

# select_sort(lst)
# print('lst:', lst)


def bubble_sort(lst):
    a = len(lst)
    for i in range(a):
        for j in range(1, a-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]


bubble_sort(lst)
print('lst:', lst)
