#Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
#и проверить тип и содержание соответствующих переменных.
#Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
#и также проверить тип и содержимое переменных.

var = ['разработка', 'сокет', 'декоратор']

for line in var:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))