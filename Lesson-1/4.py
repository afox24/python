number = input('Введите число: ')
x_max = 0
i = 0
while i < len(number):
    if int(number[i]) > x_max:
        x_max = int(number[i])
    i+=1

print(x_max)