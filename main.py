"""
 _____         _      __  
|_   _|       | |    /  | 
  | | __ _ ___| | __ `| | 
  | |/ _` / __| |/ /  | | 
  | | (_| \__ \   <  _| |_
  \_/\__,_|___/_|\_\ \___/

Напишите программу, которая выводит в консоль "Hello world"

hint: что такое print?
"""


# print("Hello world")


"""
 _____         _      _____ 
|_   _|       | |    / __  \
  | | __ _ ___| | __ `' / /'
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /___
  \_/\__,_|___/_|\_\ \_____/

Напишите рограмму, которая выводит числа от 1 до введенного пользователем. Для чисел, кратных 3, выводится "Fizz",'
для кратных 5 — "Buzz", а для чисел, кратных 3 и 5 — "FizzBuzz"

hint: цикл, если и "%"
"""


# n = int(input("Введите число: "))
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


"""
 _____         _      _____ 
|_   _|       | |    |____ |
  | | __ _ ___| | __     / /
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  .___/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая проверяет, является ли введенный пользователем год високосным

hint: https://ru.wikihow.com/%D0%B2%D1%8B%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B5-%D0%B3%D0%BE%D0%B4%D1%8B
"""


# year = int(input("Введите год: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Год високосный")
# else:
#     print("Год не високосный")


"""
 _____         _        ___ 
|_   _|       | |      /   |
  | | __ _ ___| | __  / /| |
  | |/ _` / __| |/ / / /_| |
  | | (_| \__ \   <  \___  |
  \_/\__,_|___/_|\_\     |_/

Напишите программау, которая проверяет, является ли введенная пользователем строка или число палиндромом, то есть читается ли оно одинаково с обеих сторон

hint: https://letpy.com/handbook/builtins/reversed/
"""


# s = input("Введите строку или число: ")
# if s == s[::-1]:
#     print("Это палиндром")
# else:
#     print("Это не палиндром")

"""
 _____         _      _____ 
|_   _|       | |    |  ___|
  | | __ _ ___| | __ |___ \ 
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  /\__/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая запрашивает число у пользователя и вычисляет факториал заданного числа, используя цикл или рекурсию

hint: https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB
"""


# n = int(input("Введите число: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(f"Факториал {n} = {factorial}")


"""
 _____         _       ____ 
|_   _|       | |     / ___|
  | | __ _ ___| | __ / /___ 
  | |/ _` / __| |/ / | ___ \
  | | (_| \__ \   <  | \_/ |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая проверяет, является ли число простым (делится только на 1 и само на себя). Используйте перебор делителей.

hint: x <= 1 - не простые числа
hint 2: %
"""


# n = int(input("Введите число: "))
# is_prime = True

# if n < 2:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{n} является простым числом")
# else:
#     print(f"{n} не является простым числом")


"""
 _____         _      ______
|_   _|       | |    |___  /
  | | __ _ ___| | __    / / 
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /   
  \_/\__,_|___/_|\_\ \_/    

Напишите программу, которая находит сумму всех цифр числа

hint: циклы
"""


# n = input("Введите число: ")
# sum_of_digits = sum(int(digit) for digit in n)
# print(f"Сумма цифр числа {n} = {sum_of_digits}")


"""
 _____         _      _____ 
|_   _|       | |    |  _  |
  | | __ _ ___| | __  \ V / 
  | |/ _` / __| |/ /  / _ \ 
  | | (_| \__ \   <  | |_| |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая генерирует последовательность Фибоначчи до указанного числа или количества элементов

hint: 1, 1, 2, 3 https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
hint 2: попробуйте решить с помощью рекурсии
"""


# n = int(input("Введите количество элементов Фибоначчи: "))
# fib_sequence = [0, 1]
# for i in range(2, n):
#     fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

# print(f"Последовательность Фибоначчи: {fib_sequence[:n]}")


def fibonacci_until(max_value, fib_sequence=None):
    if fib_sequence is None:
        fib_sequence = [1, 1]
    else:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib <= max_value:
            fib_sequence.append(next_fib)
        else:
            return fib_sequence
    
    return fibonacci_until(max_value, fib_sequence)

# Пример использования
max_value = int(input("Введите максимальное значение для последовательности Фибоначчи: "))
print(f"Последовательность Фибоначчи до {max_value}: {fibonacci_until(max_value)}")




