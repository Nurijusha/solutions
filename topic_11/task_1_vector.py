"""
Модуль 11. Задача 1.
Вектор.

Реализовать класс Position для работы с векторами.
Класс должен содержать атрибуты x и y.
Перегрузить операторы:
    __add__, __sub__, __mul__,__floordiv__,__truediv__, __mod__.
"""
class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Position(self.x * other.x, self.y * other.y)

    def __floordiv__(self, other):
        return Position(self.x // other.x, self.y // other.y)

    def __truediv__(self, other):
        return Position(self.x / other.x, self.y / other.y)

    def __mod__(self, other):
        return Position(self.x % other.x, self.y % other.y)
