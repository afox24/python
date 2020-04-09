# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
# Пыталась тут решить с помощью рекурсии

def sum_numbers(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

numbers = input('Введите числа через пробел: ').split()

max_n = 0
max_s = 0
for i in list_number:
    if sum_numbers(i) > max_s:
        max_n = i
        max_s = sum_numbers(i)

print(f'У числа {max_n} наибольшая сумма цифр - {max_s}')
