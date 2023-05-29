# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import math

print("Введите число N:", end="")
n = input()
if n.isdigit():
    n = int(n)
    result = counter = 0
    while result <= n:
        print(result, end = " ")
        result = pow(2, counter)
        counter += 1
else:
    print("Ошибка ввода!")
