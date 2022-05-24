import random
import time

from scripts.random_string_list import random_string_list


def search_binary_simple(order_list, key):
    """
    Функция бинарного поиска.
    В функцию подается отсортированный массив и ключ.
    Функция возращает индекс найденного элемента в списке или -1.
    Если элементы в массиве не уникальны, то возвратиться индекс
    того элемента, который попадеться при поиске первым
    (не обязательно первый по порядку одинаковых элементов).
    """
    low = 0
    high = len(order_list) -1

    while low <= high:
        middle = (high + low) // 2
        if key == order_list[middle]:
            return middle
        if key > order_list[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return -1

order_list = [0,1,2,3,4,5, 5, 5, 5, 5,6,7,8,9]
print(search_binary_simple(order_list, 5))

'''
проверка скорости выполнения бинарного поиска и встроенного поиска индекса в списке
создается большой список случайных строк, из него берется случайный элемент и и проводится его поиск.
Как итог - бинарный поиск быстрее. 
'''
maximum = 1000
spisok = sorted(random_string_list(maximum, 20))
find_elements = spisok[random.randint(0, maximum-1)]

start_func = time.perf_counter()
print(search_binary_simple(spisok, find_elements))
stop_func = time.perf_counter()
print(f'Время выполнения функции бинарного поиска: {round(stop_func-start_func, 5)}')
print()

start_func = time.perf_counter()
print(spisok.index(find_elements))
stop_func = time.perf_counter()
print(f'Время выполнения встроенной функции поиска: {round(stop_func-start_func, 5)}')

