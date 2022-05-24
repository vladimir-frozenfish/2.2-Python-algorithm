'''
Функция бинарного поиска.
В функцию подается отсортированный массив и ключ.
Функция возращает левую и правую границу ключа (ключей) в массиве
'''


def left_bound(A: list, key):
    left = -1
    right = len(A)

    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle

    return left


def right_bound(A: list, key):
    left = -1
    right = len(A)

    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle

    return right


def search_binary(A: list, key):
    A = A
    key = key
    search_result = [0, 0]
    search_result[0], search_result[1] = left_bound(A, key), right_bound(A, key)
    return search_result


A = [1, 1, 1, 4, 4, 4, 5, 7, 8, 10, 11, 23, 25]
print(search_binary(A, 30))



