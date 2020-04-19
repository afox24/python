# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import Counter

number_companies = int(input('Введите количествово компаний: '))

companies = []

for i in range(number_companies):
    title = input('Введите название компании: ')
    q1, q2, q3, q4 = map(int, input('Введите квартальные прибыли через пробел: ').split(' '))
    a = {
        'Название компании': title,
        'Квартал 1': q1,
        'Квартал 2': q2,
        'Квартал 3': q3,
        'Квартал 4': q4,
        'Прибыль за год': q1 + q2 + q3 + q4,
    }

    companies.append(a)

profit_c = Counter()
for a in companies:
    profit_company = a.copy()
    del profit_company['Название компании']
    profit_c += Counter(profit_company)

print()
for a in companies:
    print(a)

avg = profit_c['Прибыль за год'] // len(companies)

print('Сумма прибыли всех компаний: ', profit_c)
print('Средняя годовая прибыль компаний: ', avg)
print('Прибыль выше среднего: ', [x['Название компании'] for x in companies if x['Прибыль за год'] >= avg])
print('Прибыль ниже среднего: ', [x['Название компании'] for x in companies if x['Прибыль за год'] < avg])