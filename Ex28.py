# Задача28. Напишите рекурсивную функцию sum(a, b), возвращающую
# сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать
# циклы.

def summa(num1: int, num2: int):
    if num2 == 0:
        return num1
    else:
        print('Call')
        return summa(num1+1, num2-1)


a = int(input('Введите первое слагаемое: '))
b = int(input('Введите второе слагаемое: '))

if(a > b):
    print(summa(a, b))
else: 
    print(summa(b, a))