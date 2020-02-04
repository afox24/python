def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 0
my_numbers = []
for el in fibo_gen(5):
    if i > 15:
        break
    else:
        my_numbers.append(el)
        i += 1
print(my_numbers)