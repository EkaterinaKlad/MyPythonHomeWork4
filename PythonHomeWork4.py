
# Задача 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
# Известно, что при хранении данных используется принцип: одна строка — один пользователь. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, 
# значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи


# file_1 = open('users.txt', 'r', encoding='utf-8')
# keys = file_1.readlines() 
# print(keys) 
# file_1.close()
# print(file_1.closed)

# file_2 = open('hobby.txt', 'r', encoding='utf-8')
# val = file_2.readlines()
# print(val)
# file_2.close()
# print(file_2.closed)

# my_dict = {}
# my_dict = dict(zip(keys, val))

# with open('users_hobby.txt', 'w', encoding='utf-8') as my_file:    
#     print(my_dict, sep='\n', file=my_file)

# print(my_dict)



# Задача 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# num = int(input("Введите число: "))
# i = 2 # первое простое число
# list = []
# a = num
# while i <= num:
#     if num % i == 0:
#         list.append(i)
#         num //= i
#         # i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {a}: {list}")



# Задача 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

# list = [int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
# print(list)

# my_list = []
# for i in list:
#     if i not in my_list:
#         my_list.append(i)

# print(f"Список неповторяющихся элементов: {my_list}")



# Задача 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

k = int(input("Введите натуральную степень k: "))
from random import randint as rd
a = rd(0, 100)
b = rd(0, 100)
c = rd(0, 100)

f = a*(x**k) + b*x + c
f = 0



# Задача 34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0


# a = [2, 4, 5]
# b = [1, 5, 3]

# list = []
# i = 0
# for i in range(0, 3):
#     list.append(a[i] + b[i])    
# print(list)    









