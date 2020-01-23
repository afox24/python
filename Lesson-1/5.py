revenue = int(input('Введите выручку: '))
outlay = int(input('Введите издержки: '))
if revenue > outlay:
    profit = revenue - outlay
    profitability = profit / revenue * 100
    print('Ваша компания просто супер!')
else:
    print('Работайте лучше!')

