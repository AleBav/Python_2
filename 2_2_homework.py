# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions

num1 = int(input("Введите числитель первой дроби: "))
den1 = int(input("Введите знаменатель первой дроби: "))

num2 = int(input("Введите числитель второй дроби: "))  
den2 = int(input("Введите знаменатель второй дроби: "))    

print("Модуль fractions выдаёт произведение дробей: ")
print(((fractions.Fraction(num1, den1) * fractions.Fraction(num2, den2))))
print("Модуль fractions выдаёт сложение дробей: ")
print(((fractions.Fraction(num1, den1) + fractions.Fraction(num2, den2))))


