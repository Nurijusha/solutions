"""
Модуль 10. Задача 7.
Внутри шара.

На вход программе подаются три строки текста с вещественными числами, значениями
абсцисс (x), ординат (y) и аппликат (z) точек трехмерного пространства. Напишите
программу для проверки расположения всех точек с введенными координатами внутри
либо на поверхности шара с центром в начале координат и радиусом R = 2.

Формат входных данных:
Подаются три строки текста с вещественными числами, разделенными символом
пробела – абсциссы, ординаты и аппликаты точек в трехмерной системе координат.

Формат выходных данных:
Вывести True если все точки с введенными координатами находятся внутри или
на границе шара и False, если вне.
"""
abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]

print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))
