# Задача 26:  Напишите программу, которая на вход принимает
# два числа A и B,и возводит число А в целую степень B
# с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
def degree(numbA, numbB):
    if numbB == 0:
        return 1
    return numbA * degree(numbA, numbB - 1)


A = int(input("Input number A :"))
B = int(input("Input number B :"))
print(f'Result of degree {A} in number {B} is : {degree(A, B)}')
