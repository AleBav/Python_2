# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num_1 = int(input("Введите целое число: ")) 

def to_hex(num):
    hex_chars = "0123456789abcdef"
    hex_string = ""
    
    while num > 0:
        remainder = num % 16
        hex_string = hex_chars[remainder] + hex_string
        num = num // 16
    
    return hex_string

print ("Функция to_hex выдаёт число: " + to_hex(num = num_1))

print ("Готовая функция hex выдаёт число: " + (hex(num_1) [2:]))
num_hex = int(num_1) 

