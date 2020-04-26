# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

n = 5
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * n + 1)]

def gnome_sort(arr):
    i, size = 1, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr

def median(arr, left, right):
    arr = arr.copy()
    a = len(arr) // 2

    if left >= right:
        return arr[a]

    pivot = arr[a]
    i = left
    j = right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if a < i:
        arr[a] = median(arr, left, j)
    elif j < a:
        arr[a] = median(arr, i, right)
    return arr[a]


print(f'Исходный массив {array}')
print(f'Отсортированный массив: {gnome_sort(array)}')
median = median(array, 0, len(array) - 1)
print(f'Медиана: {median}')
