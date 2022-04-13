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
            # for m in range(k*2, N+1, k):
            for m in range(k*k, N + 1, k):  # лучше начинать с квадрата числа, так как удвоение уже будут False
                A[m] = False

    return A


def get_least_primes_linear(n):
    """поиск простых чисел, с помощью линейного решета
    Алгоритм такой:
    Для каждого числа i будем хранить lp[i] — минимальный простой делитель числа i. Заведём массив lp длины n + 1.
    А также массив primes, в который будем добавлять найденные простые числа.
    Перебираем i по возрастанию.
    Если lp[i] = 0, можно сделать вывод, что число i простое, и добавить его в массив primes.
    Рассматриваем все простые числа p, которые не больше lp[i]. Обновляем lp[p * i] = p.
    """
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


N = int(input('Введите диапазон N: '))
list_simple = resheto_eratosfen(N)

for i in range(2, len(list_simple)):
    print(f'Число {i} -', 'простое' if list_simple[i] else 'составное')

print(get_least_primes_linear(20))
