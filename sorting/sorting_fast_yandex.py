from random import randint


def partition(array, pivot):
    left = []
    center = []
    right = []
    for volume in array:
        if volume < pivot:
            left.append(volume)
        elif volume > pivot:
            right.append(volume)
        else:
            center.append(volume)
    return left, center, right


def quicksort(array):
    if len(array) < 2:      # базовый случай,
        return array        # массивы с 0 или 1 элементами фактически отсортированы
    else:                   # рекурсивный случай
        pivot = array[randint(0, len(array) - 1)]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


random_list = [randint(0, 50) for i in range(10)]
print('Неотсортированный массив: ', random_list)
sorting_list = quicksort(random_list)
print('Отсортированный массив: ', sorting_list)

