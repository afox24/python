a = float(input("Первый день: "))
b = float(input("Последний день: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    a += 1
    print(day)