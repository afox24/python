# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

mn = 0
mx = 0
for i in range(1, SIZE):
    if i < mn:
        mn = i
    elif i > mx:
        mx = i
print(f'Минимальное число: {array[mn]}, максимальное число: {array[mx]}')
if mn > mx:
    mn, mx = mx, mn
summ = 0
for i in range(mn+1, mx):
    summ += array[i]
print(f'Сумма элементов, между минимальным и максимальным элементами: {summ}')