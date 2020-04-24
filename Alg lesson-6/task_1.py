# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти

# macOS (разряд, скорее всего, 64), Python 3.8

# Определить, какое число в массиве встречается чаще всего.


import random
import sys

# Подсчет памяти (надеюсь можно было использовать функцию из лекции)

def show(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#print('Массив:', array, sep='\n')

# 1 вариант
# Только list

n = 0
for i in array:
   if array.count(n) < array.count(i):
        n = array.index(i)
        #print(f'Число {array[n]}, встречается {array.count(n)} раза')

#print(show(array))
#print(show(n))
#print(show(SIZE))
#print(show(MIN_ITEM))
#print(show(MAX_ITEM))
#print(show(i))

# Общая занимаемая память = 600

# 2 вариант
# С list генерим массив, с dict выводим число: кол-во в массиве

n = dict()

for i in array:
    if i not in n:
        n[i] = 1
    else:
        n[i] += 1

#print(f'Повторения чисел в массиве:\n{n}')

count = 0
num_count = []

for num in n:

    if n[num] > count:
        count = n[num]
        num_count = [num]

    elif n[num] == count:
        num_count.append(num)

#print('\nЧаще всего встречается:', end=' ')
#print(*num_count)
#print(f'Количество повторений: {count}')

#print(show(n))
#print(show(SIZE))
#print(show(MIN_ITEM))
#print(show(MAX_ITEM))
#print(show(i))
#print(show(count))
#print(show(num_count))

# Общая занимаемая память = 1 992


# 3 вариант
# Самописный tuple

tuple = (35, 758, 0, 98, 758, 90, 0, 456, 90, 1, 6, 90)

mx_n = 0
for i in tuple:
    n = 0
    for j in tuple:
        if j == i:
            n += 1
    if mx_n < n:
        mx_n = n
        a = i

#print(tuple)
#if mx_n > 1:
    #print(f"Число {a}, Кол-во повторений {mx_n}")
#else:
    #print('Все числа уникальны')

#print(show(tuple))
#print(show(mx_n))
#print(show(n))
#print(show(i))
#print(show(j))
#print(show(a))

# Общая занимаемая память = 604

# Вывод: меньше всего память занял первый вариант с использованием list.
# Но думаю, если оптимизировать код и использовать tuple, то будет преимущетсво в занимаемой памяти перед list.
