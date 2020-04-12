# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

n = 0
for i in array:
    if array.count(n) < array.count(i):
        n = array.index(i)

print(f'Число {array[n]}, встречается {array.count(n)} раза')