my_str = input('Введите предложение: ')
x = my_str.split(' ')
for i, word in enumerate(x, 1):
    if len(word) > 10:
        word = word[0:10]
    print(f"{i}. - {word}")
