from sys import argv

script_name, work_hour, rate_hour, bonus = argv

result = (int(work_hour) * (int(rate_hour)) + int(bonus))
print(f'Ваша зарплата: {result}')