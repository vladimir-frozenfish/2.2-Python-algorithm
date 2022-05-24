def insertion_sort(unsort_array):
    """
    сортировка вставками O(n**2), сортировка вставками - устойчивая.
    возвращает новый отсортированный массив, поданный в функцию не трогает
    """
    array = list(unsort_array)
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
        # print(f'step {i}, sorted {i+1} elements: {array}')
    return array


unsort_array = [9, 4, 2, 1, 3, 0]
sort_array = insertion_sort(unsort_array)
print(unsort_array)
print(sort_array)
