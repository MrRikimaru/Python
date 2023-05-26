# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

print("Введите натуральное число:", end="")
number = input()
if (number.isdigit()) & (len(str(number)) == 6):
    number = int(number)
    temp = number
    fistPart = secondPart = 0
    numberLenght = len(str(number))
    for i in range(numberLenght):
        if i < numberLenght // 2:
            fistPart += temp % 10
        else:
            secondPart += temp % 10
        temp //= 10
    if fistPart == secondPart:
        print(True)
    else:
        print(False)
else:
    print("Ошибка ввода!")
