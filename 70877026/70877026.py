# -*- coding: UTF-8 -*-
from itertools import groupby
from math import nan


def group_by_type():
    data = [1, 2, 3, nan, nan, nan, 4, 5, 6, nan, nan, 7, nan, 8, 9]
    g = groupby(data, key=type)  # group by type of the data, int != float
    result = [list(item[1]) for item in g if item[0] == int]
    print(result)  # [[example.txt, 2, 3], [4, 5, 6], [7], [8, 9]]


def group_by_func():
    data = [("age", 12), ("age", 13), ("name", "beer")]
    g = groupby(data, lambda x: x[0])
    result = {item[0]: list(item[1]) for item in g}
    print(result)  # {'age': [('age', 12), ('age', 13)], 'name': [('name', 'beer')]}


if __name__ == '__main__':
    group_by_type()
    group_by_func()
