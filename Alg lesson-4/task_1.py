import timeit
import cProfile


# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

# Выбрана задача 2 из Урока 2:
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# 1 вариант

def method_1(a):
    even = 0
    odd = 0
    left = a
    while True:
        left, n = divmod(left, 10)
        if n % 2:
            odd += 1
        else:
            even += 1
        if left == 0:
            break
    return (f'У числа {n}: четных цифр - {even}, нечетных - {odd} ')

#print(timeit.timeit('method_1(123456)', number=100, globals=globals()))  # 0.00023326900000000123
#print(timeit.timeit('method_1(123456123456)', number=100, globals=globals()))  # 0.0004335570000000011
#print(timeit.timeit('method_1(123456123456123456)', number=100, globals=globals()))  # 0.0007393109999999994
#print(timeit.timeit('method_1(123456123456123456123456)', number=100, globals=globals())) # 0.0009271520000000005
#print(timeit.timeit('method_1(123456123456123456123456123456)', number=100, globals=globals())) # 0.0010994429999999916

#cProfile.run('method_1(123456)')  #  6    0.000    0.000    0.000    0.000 {built-in method builtins.divmod}
#cProfile.run('method_1(123456123456)')  # 12    0.000    0.000    0.000    0.000 {built-in method builtins.divmod}
#cProfile.run('method_1(123456123456123456)')  # 18    0.000    0.000    0.000    0.000 {built-in method builtins.divmod}
#cProfile.run('method_1(123456123456123456123456)') # 24    0.000    0.000    0.000    0.000 {built-in method builtins.divmod}
#cProfile.run('method_1(123456123456123456123456123456)') #  30    0.000    0.000    0.000    0.000 {built-in method builtins.divmod}

# Вывод: данный метод имеет квадратичную сложность, а так же вызов функции увеличивался с шагом 6 при каждой попытке вызова.
# Не самый оптимальный вариант для решения данной задачи.


# 2 вариант

def method_2(n, even=0, odd=0):
    if n == 0:
        return even, odd
    else:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            even += 1
            return method_2(n, even, odd)
        else:
            odd += 1
            return method_2(n, even, odd)

#print(timeit.timeit('method_2(123456)', number=100, globals=globals()))  # 0.00016648699999999989
#print(timeit.timeit('method_2(123456123456)', number=100, globals=globals()))  # 0.00032462199999999664
#print(timeit.timeit('method_2(123456123456123456)', number=100, globals=globals()))  # 0.0004987600000000009
#print(timeit.timeit('method_2(123456123456123456123456)', number=100, globals=globals())) # 0.0010553110000000032
#print(timeit.timeit('method_2(123456123456123456123456123456)', number=100, globals=globals())) # 0.0008889540000000043

#cProfile.run('method_2(123456)')  #  7/1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)
#cProfile.run('method_2(123456123456)')  # 13/1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)
#cProfile.run('method_2(123456123456123456)')  # 19/1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)
#cProfile.run('method_2(123456123456123456123456)') # 25/1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)
#cProfile.run('method_2(123456123456123456123456123456)') #  31/1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)

# Вывод: данный метод имеет квадратичную сложность, а так же вызов функции увеличивался с шагом 6 при каждой попытке вызова.
# Не самый оптимальный вариант для решения данной задачи. Аналогичен с вариантом 1.


# 3 вариант

def memorize(func):
    def g (n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def method_3(n, even=0, odd=0):
    if n == 0:
        return even, odd
    else:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            even += 1
            return method_2(n, even, odd)
        else:
            odd += 1
            return method_2(n, even, odd)


#print(timeit.timeit('method_3(123456)', number=100, globals=globals()))  # 5.68749999999979e-05
#print(timeit.timeit('method_3(123456123456)', number=100, globals=globals()))  # 5.343799999999593e-05
#print(timeit.timeit('method_3(123456123456123456)', number=100, globals=globals()))  # 4.532799999999726e-05
#print(timeit.timeit('method_3(123456123456123456123456)', number=100, globals=globals())) # 5.17660000000017e-05
#print(timeit.timeit('method_3(123456123456123456123456123456)', number=100, globals=globals())) # 7.606500000000016e-05

#cProfile.run('method_3(123456)')  #  1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)
#cProfile.run('method_3(123456123456)')  # 1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)
#cProfile.run('method_3(123456123456123456)')  # 1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)
#cProfile.run('method_3(123456123456123456123456)') # 1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)
#cProfile.run('method_3(123456123456123456123456123456)') #  1    0.000    0.000    0.000    0.000 task_1.py:43(method_2)

# Вывод: алгоритм выполняется практически за константное время.
# по cProfile не видно слабых мест метода.
# Можно считать этот метод самым оптимальным для решения задачи.