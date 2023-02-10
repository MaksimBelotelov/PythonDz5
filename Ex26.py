# Напишите программу, которая на вход принимает два числа А и В
# и возводит число А в целую степень В с помощью рекурсии

def pow(number: int, ex: int):
    if ex == 0:
        return 1
    else:
        return number*pow(number, ex-1)

a = int(input('Введите число: '))
b = int(input('Введите степень, в которую возвести: '))

print(pow(a, b))
