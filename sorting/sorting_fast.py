import random

def quick_sort(array):
    """алгоритм быстрой сортировки
    O(n**2) - в худшем случае
    O(n*log(n)) - в среднем
    в данной функции опорный элемент выбирается первым из массива - это не самы хороший вариант,
    лучше выбирать опорный элемент случайным образом (или можно из середины)"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]                                # опорный элемент
        less = [i for i in array[1:] if i <= pivot]     # подмассив всех элементов, меньших опорного
        greater = [i for i in array[1:] if i > pivot]   # подмассив всех элементов, больших опорного
        print(f'{less} + {pivot} + {greater}')          # показывается как работает рекурсия сортировки
        return quick_sort(less) + [pivot] + quick_sort(greater)


random_list = [random.randint(0, 50) for i in range(10)]
print('Неотсортированный массив: ', random_list)
sorting_list = quick_sort(random_list)
print('Отсортированный массив: ', sorting_list)
