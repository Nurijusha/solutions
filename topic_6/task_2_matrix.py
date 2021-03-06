"""
Модуль 6. Задача 2.
Матрица.

На вход программе подаются два натуральных числа n и m. Напишите программу,
которая создает матрицу размером n×m и заполняет её числами от 1 до n⋅m в
соответствии с образцом.

Формат входных данных:
На одной строке подаются два натуральных числа n и m — количество строк и
столбцов в матрице.

Формат выходных данных:
Вывести матрицу в соответствии с образцом.
Например:
1  2  3  4
5  6  7  8
9  10 11 12
"""
n, m = map(int, input().split())
matrix = []
counter = 1

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(counter)
        counter += 1

        print(f'{matrix[i][j]}'.ljust(3), end='')
    print()
