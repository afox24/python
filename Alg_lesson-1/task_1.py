# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
n = input("Введите трехзначное число: ")
n = int(n)
n1 = n % 10
n2 = n % 100 // 10
n3 = n // 100
summ = n1 + n2 + n3
prod = n1 * n2 * n3
print(f'Сумма цифр числа: {summ}')
print(f'Произведение цифр числа: {prod}')