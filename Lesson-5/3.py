my_f = open('test_3', 'r')
content = my_f.readlines()
for line in content:
    name, salary = line.split()
    i = int(salary)
    if i < 20000:
        print(f'Зарплата меньше 20000 {name, int(salary)}, средний оклад {sum(map(int, salary)) / len(salary)}')

