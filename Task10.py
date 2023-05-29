# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

print("Введите количество монет:", end="")
count = input()
first = second = 0
zeroCounter = oneCounter = 0
if count.isdigit():
    count = int(count)
    print("Введите состояние монеты 0/1:")
    for i in range(count):
        status = int(input())
        if status == 0:
            zeroCounter += 1
        elif status == 1:
            oneCounter += 1
        else:
            print("Ошибка ввода!")
if zeroCounter < oneCounter:
    print(f"Минимальное число монет, которые нужно перевернуть равно: {zeroCounter}")
else:
    print(f"Минимальное число монет, которые нужно перевернуть равно: {oneCounter}")
