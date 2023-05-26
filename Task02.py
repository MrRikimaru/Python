# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("Введите число:", end="")
number = input()
if (number.isdigit()):
    temp = int(number)
    result = 0
    while temp > 0:
        result += temp % 10
        temp //= 10
    print(f"{number} -> {result}")
else:
    print("Ошибка ввода!")