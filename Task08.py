# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один 
# разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

print("Введите значение n:", end = "")
nValue = input()
print("Введите значение m:", end = "")
mValue = input()
print("Введите значение k:", end = "")
kValue = input()
if (nValue.isdigit()) & (mValue.isdigit()) & (kValue.isdigit()):
    nValue = int(nValue)
    mValue = int(mValue)
    kValue = int(kValue)
    if kValue < nValue*mValue:
        if kValue // nValue * nValue == kValue:
            print(True)
        elif kValue // mValue * mValue == kValue:
            print(True)
        else:
            print(False)
else:
    print("Ошибка ввода!")
