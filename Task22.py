# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами
# элементы множеств.

n = input("Введите количество элементов 1-ого множества:")
if n.isdigit():
    m = input("Введите количество элементов 2-ого множества:")
    if m.isdigit():
        n, m = int(n), int(m)
        enumN = []
        enumM = []
        print("Заполните первое множество натуральными числами:")
        for i in range(n):
            enumN.append(input())
        print("Заполните второе множество натуральными числами:")
        for i in range(m):
            enumM.append(input())
        enumN.sort()
        enumM.sort()
        print(f"{enumN}\n{enumM}")
        enumMerge = []
        for i in range(n):
            for j in range(m):
                if enumN[i] == enumM[j]:
                    if len(enumMerge) > 0:
                        if enumMerge[len(enumMerge) - 1] != enumN[i]:
                            enumMerge.append(enumN[i])
                    else:
                        enumMerge.append(enumN[i])
        print(enumMerge)


else:
    print("Ошибка ввода!")
