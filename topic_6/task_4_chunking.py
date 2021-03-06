"""
Модуль 6. Задача 4.
Разбиение на чанки.

На вход программе подаются две строки, на одной символы, на другой число n.
Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число,
задающее размер чанка (куска), а возвращает список из чанков указанной длины.

Формат входных данных:
Подается строка текста, содержащая символы, отделенные символом пробела
и число n на отдельной строке.

Формат выходных данных:
Вывести указанный вложенный список.
"""


def chunked(stroka, number):
    chunk = []
    while len(stroka) > 0:
        chunk.append(stroka[:n])
        stroka = stroka[n:]
    return chunk


s = input().split()
n = int(input())

print(chunked(s, n))
