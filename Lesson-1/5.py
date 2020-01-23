revenue = int(input('Введите выручку: '))
outlay = int(input('Введите издержки: '))
if revenue > outlay:
    profit = revenue - outlay
    rentability = profit / revenue
    print(F'Ваша компания просто супер!')
else:
    print('Работайте лучше!')
worker = int(input("Как много человек работает: "))
print(f"{profit/worker} на одного работника")
