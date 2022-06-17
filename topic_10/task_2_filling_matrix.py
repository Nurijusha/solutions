"""
Модуль 10. Задача 2.
Заполнение матрицы.

Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу
заданного размера. При этом (в зависимости от переданных аргументов) она
должна вести себя так:
    matrix() — возвращает матрицу 1× 1, в которой единственное число равно нулю
    matrix(n) — возвращает матрицу n× n, заполненную нулями;
    matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями;
    matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой
каждый элемент равен числу value.
При создании функции пользуйтесь аргументами по умолчанию.

Формат выходных данных:
Только реализовать, ничего выводить не нужно.
"""
def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value] * m for _ in range(n)]
