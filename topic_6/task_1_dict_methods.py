"""
Модуль 6. Задача 1.
Методы словаря.

Имеется словарь с наименованиями предметов и их весом (в граммах):
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400,
          'удочка': 1200, 'расческа': 40, 'котелок': 820, 'палатка': 5240,
          'брезент': 2130, 'спички': 10}
Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный
вес в N кг (вводится с клавиатуры).Он решил класть в рюкзак предметы в порядке
убывания их веса (сначала самые тяжелые, затем, все более легкие) так,
чтобы их суммарный вес не превысил значения N кг. Все предметы даны в
единственном экземпляре.Выведите список предметов (в строчку через пробел),
которые берет с собой Сергей в порядке убывания их веса.

Формат входных данных:
Натуральное число.

Формат выходных данных:
Список через пробел.
"""
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

weidth = int(input()) * 1000
weidth_in_backpack = sorted([inventory for inventory in things.values()], reverse=True)

inventory_in_way = []
for i in range(len(weidth_in_backpack)):
    for key, val in things.items():
        if weidth - val >= 0:
            if val == weidth_in_backpack[i]:
                # print(key, end=' ')
                inventory_in_way.append(key)
                weidth -= val
                break

print(*inventory_in_way)
