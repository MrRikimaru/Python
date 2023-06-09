# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def recursion(a, b):
    if (a == 1) | (b == 0):
        return 1
    if (b > 1):
        return a * recursion(a, b-1)
    if (b > 1):
        return 1/a * recursion(a,b+1)
    return a

nmbrA = int(input("Введите основание:"))
nmbrB = int(input("Введите степень:"))
print(f'{nmbrA}^{nmbrB} = {recursion(nmbrA,nmbrB)}')