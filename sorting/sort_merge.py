import random

def merge_sort(array):
    """функиця сортировки слиянием - O(n*log(n))
    алгоритм устойчивый"""
    len_array = len(array)
    if len_array == 1:  # базовый случай рекурсии
        return array

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: len_array // 2])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[len_array // 2: len_array])

    # заводим массив для результата сортировки
    result = [0] * len_array

    # сливаем результаты
    l, r, k = 0, 0, 0
    len_left = len(left)
    len_right = len(right)
    while l < len_left and r < len_right:
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len_left:
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1
    while r < len_right:
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result

random_list = [random.randint(0, 5000) for i in range(1000)]
print('Неотсортированный массив: ', random_list)
sorting_list = merge_sort(random_list)
print('Отсортированный массив: ', sorting_list)