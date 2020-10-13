import json
import re


def write_order_to_json(item, quantity, price, buyer, date, is_first):
    dict_ = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}

    with open('orders.json', 'r+') as json_file:
        json_file.seek(12)
        end_ = json_file.readlines()
        json_file.seek(12)
        json.dump(dict_, json_file, indent=4)
        if not is_first:
            json_file.write(',')
        json_file.writelines(end_)


add_pattern = '^[aA][dD][dD]$'
exit_pattern = '^[eE][xX][iI][tT]$'
is_first = True

while True:
    print('Для добавления товара введите \"Add\", чтобы выйти \"Exit\"')
    answer = input()
    if re.match(exit_pattern, answer):
        break
    if re.match(add_pattern, answer):
        item = input('Введите название товара: ')
        quantity = int(input('Введите количество: '))
        price = float(input('Введите цену: '))
        buyer = input('Введите ФИО покупателя: ')
        date = input('Введите дату покупки: ')
        write_order_to_json(item, quantity, price, buyer, date, is_first)
        is_first = False
