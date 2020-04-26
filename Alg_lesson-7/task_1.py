# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def bubble_sort(arr):
    left = len(arr) - 1
    right = 1
    while right <= left:
        if arr[right] > arr[right-1]:
            [arr[right], arr[right-1]] = [arr[right-1], arr[right]]
        if right == left:
            right = 0
            left -= 1
        right += 1
    return arr

print(f'Исходный массив: {array}')
print(f'Отсортированный массив: {bubble_sort(array)}')