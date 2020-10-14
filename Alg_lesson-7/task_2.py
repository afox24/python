# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
LIMIT = 3
MIN_ITEM = 0
MAX_ITEM = 49
array = [round(random.uniform(0, 49), LIMIT) for _ in range(SIZE)]

def merge(left, right):
    sort = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sort.append(left[i])
            i += 1
        else:
            sort.append(right[j])
            j += 1

    sort += left[i:]
    sort += right[j:]
    return sort

def merge_sort(arr):

    if len(arr) < 2:
        return arr

    middle = len(arr) // 2

    left_list = arr[:middle]
    right_list = arr[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(left_list, right_list)

print(f'Исходный массив: {array}')
print(f'Отсортированный массив: {merge_sort(array)}')