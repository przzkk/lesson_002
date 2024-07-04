#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код

garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
# TODO здесь ваш код

all_type_flowers = garden_set | meadow_set
print(all_type_flowers)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код

flower_crossings = garden_set & meadow_set
print(flower_crossings)


# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
garden_only = garden_set - meadow_set
print(garden_only)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
meadow_only = meadow_set - garden_set
print(meadow_only)


