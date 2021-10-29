def insert_sort(A):
    """ сортировка списка A вставками """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choise_sort(A):
    """ сортировка списка A выбором """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    """ сортировка списка A методом пузырька """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

def test_sort(sort_algorithm):
    ''' тестирующая функиця '''
    print('Тестируем:', sort_algorithm.__doc__)
    print("testcase #1: ", end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')

    print("testcase #2: ", end='')
    A = [2, 2, 2, 1, 2]
    A_sorted = [1, 2, 2, 2, 2]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
