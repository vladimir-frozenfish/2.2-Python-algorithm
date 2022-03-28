"""
алгоритм сортировки выбором O(n**2)
"""

import time

from scripts.random import random_string_list


def minimum(array):
    """функция возвращает индекс наименьшего элемента в массиве (списке)"""
    minimum = array[0]
    minimum_index = 0

    for i in range(1, len(array)):
        if array[i] < minimum:
            minimum = array[i]
            minimum_index = i
    return minimum_index


def selection_sort(array):
    """функция возвращает новый отсортированный список"""
    sort_array = []
    while len(array) > 0:
        sort_array.append(array.pop(minimum(array)))
    return sort_array


def selection_sort_2(array):
    """функция возвращает новый отсортированный список,
    минимальное значение переставляется в текущем массиве"""
    for i in range(len(array)):
        min_index = minimum(array[i:])
        array[i], array[min_index+i] = array[min_index+i], array[i]
    return array


array = random_string_list(10, 5,  symbols='абвгд')
array2 = list(array)
print(array)
print(selection_sort(array))
print(selection_sort_2(array2))
print()

'''
проверка скорости выполнения сортировки выбором и встроенной сортировки
встроенная сортировка быстрее
'''
maximum = 10000
spisok1 = random_string_list(maximum, 20)
spisok2 = list(spisok1)
spisok3 = list(spisok1)

start_func = time.perf_counter()
# print(selection_sort(spisok1))
spisok1_sort = selection_sort(spisok1)
stop_func = time.perf_counter()
print(f'Время выполнения функции сортировки выбором: {round(stop_func-start_func, 5)}')
print()

start_func = time.perf_counter()
# print(selection_sort(spisok1))
spiso2_sort = selection_sort_2(spisok2)
stop_func = time.perf_counter()
print(f'Время выполнения функции сортировки выбором 2: {round(stop_func-start_func, 5)}')
print()

start_func = time.perf_counter()
# print(sorted(spisok2))
spiso2_sort = sorted(spisok3)
stop_func = time.perf_counter()
print(f'Время выполнения встроенной функции сортировки: {round(stop_func-start_func, 5)}')


