# Определение количества различных подстрок с использованием хеш-функции

import hashlib

string = input("Введите строку из маленьких латинских букв: ")
l = len(string)
n = set()

for i in range(l):
    if i == 0:
        l = len(string) - 1
    else:
        l = len(string)

    for j in range(l, i, -1):
        #print(string[i:j])
        n.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())

print(f"Количество различных подстрок в строке '{string}' равно {len(n)}")