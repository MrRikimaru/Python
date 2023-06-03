# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:

# 5
#     1 2 3 4 5
#     6 -> 5

from random import randint

n = input("Введите размер массива N:")
myList = []
for i in range(int(n)):
    myList.append(randint(0, 10))
    print(myList[i], end=" ")
num = input("\nВведите число:")
max = 0
for i in range(int(n)):
    if (myList[i] < int(num)):
        if myList[i] > max:
            max = myList[i]
print(f"Ближайшее по велечине к {num} число  -> {max}", end="")
