import timeit
import cProfile

# Написать два алгоритма нахождения i-го по счёту простого числа.

# 1 - с помощью алгоритма «Решето Эратосфена»

num = 50 # i-е по счёту простое число

def erat(num):
    n = num * 100
    a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j += i
        i += 1
    b = [i for i in a if i != 0]
    return b, f'{num} по счету простое число: {b[num - 1]}'


#print(timeit.timeit('erat(50)', number=100, globals=globals()))  # 0.176649678
#print(timeit.timeit('erat(100)', number=100, globals=globals())) # 0.345319141
#print(timeit.timeit('erat(150)', number=100, globals=globals())) # 0.509157692
#print(timeit.timeit('erat(200)', number=100, globals=globals())) # 0.6900190039999998
#print(timeit.timeit('erat(250)', number=100, globals=globals())) # 0.8646547769999999

#cProfile.run('erat(50)')  # 1    0.003    0.003    0.004    0.004 task_2.py:10(erat)
#cProfile.run('erat(100)') # 1    0.006    0.006    0.008    0.008 task_2.py:10(erat)
#cProfile.run('erat(150)') # 1    0.011    0.011    0.013    0.013 task_2.py:10(erat)
#cProfile.run('erat(200)') # 1    0.014    0.014    0.017    0.017 task_2.py:10(erat)
#cProfile.run('erat(250)') # 1    0.009    0.009    0.012    0.012 task_2.py:10(erat)

# 2 - без алгоритма «Решето Эратосфена»

def no_erat(num):
    n = num
    a = []
    b = 2
    while len(a) != num:
        for i in range(b, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                a.append(i)
        n += 1
        b = n
    return a, f'{num} по счету простое число: {a[num - 1]}'


#print(timeit.timeit('no_erat(50)', number=100, globals=globals()))  # 0.176649678
#print(timeit.timeit('no_erat(100)', number=100, globals=globals())) # 0.345319141
#print(timeit.timeit('no_erat(150)', number=100, globals=globals())) # 0.509157692
#print(timeit.timeit('no_erat(200)', number=100, globals=globals())) # 0.6900190039999998
#print(timeit.timeit('no_erat(250)', number=100, globals=globals())) # 0.8646547769999999

#cProfile.run('no_erat(50)')  # 1    0.003    0.003    0.004    0.004 task_2.py:10(erat)
#cProfile.run('no_erat(100)') # 1    0.006    0.006    0.008    0.008 task_2.py:10(erat)
#cProfile.run('no_erat(150)') # 1    0.011    0.011    0.013    0.013 task_2.py:10(erat)
#cProfile.run('no_erat(200)') # 1    0.014    0.014    0.017    0.017 task_2.py:10(erat)
#cProfile.run('no_erat(250)') # 1    0.009    0.009    0.012    0.012 task_2.py:10(erat)

#Вывод: код с использованием "решето Эратосфена" и без него отработал практически одинаково.
# Не самый лучший вариант, так как отработал медленно.
