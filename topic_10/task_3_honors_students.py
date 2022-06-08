"""
Модуль 10. Задача 3.
Отличники.

Учитель Тимур проверял контрольные работы по математике в нескольких классах
онлайн-школы и решил убедиться, что в каждом классе есть хотя бы один отличник–
ученик с оценкой 55 по контрольной работе. Напишите программу с использованием
встроенных функций all(), any() для помощи Тимуру в проверке.

Формат входных данных:
Подается натуральное число n – количество классов. Затем для каждого класса
вводится блок информации вида: натуральное число k – количество учеников в
классе; далее вводится k строк вида: фамилия оценка.

Формат выходных данных:
Программа должна вывести YES, если в каждом классе есть хотя бы один отличник,
и NO в противном случае.
"""
progress = []
for i in range(int(input())):
    progress.append(any(['5' in input().split() for j in range(int(input()))]))

print('YES' if all(progress) else 'NO')
