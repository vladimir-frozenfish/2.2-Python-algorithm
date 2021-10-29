def resheto_eratosfen(N: int):
    '''
    Возвращает список A с булевыми значениями,
    где True - простое число,
    False - составное
    числа соответствуют индексу списка A
    :param N: 
    :return: 
    '''

    A = [True]*(N+1)
    A[0] = A[1] = False  # числа 0 и 1 не являются простыми

    for k in range(2, N+1):
        if A[k]:
            for m in range(k*2, N+1, k):
                A[m] = False

    return A


N = int(input('Введите диапазон N: '))
list_simple = resheto_eratosfen(N)

for i in range(2, len(list_simple)):
    print(f'Число {i} -', 'простое' if list_simple[i] else 'составное')
