# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# 5
#     1 2 3 4 5
#     3 -> 1
from random import randint

n = input("Введите размер массива N:")
counter = 0
myList = []
for i in range(int(n)):
    myList.append(randint(0, 10))
    print(myList[i], end=" ")
num = input("\nВведите искомое число:")
for i in range(int(n)):
    if myList[i] == int(num):
        counter = counter + 1
print(f"{num} -> {counter}", end="")
