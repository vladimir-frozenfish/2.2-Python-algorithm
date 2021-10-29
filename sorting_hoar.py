# рекурсивная функция сортировки Тони Хоара

def hoar_sorting(A):
    if len(A) <= 1:
        return

    barier = A[0]
    left = []
    middle = []
    right = []

    for x in A:
        if x < barier:
            left.append(x)
        elif x == barier:
            middle.append(x)
        else:
            right.append(x)

    hoar_sorting(left)
    hoar_sorting(right)

    k = 0
    for x in left+middle+right:
        A[k] = x
        k += 1


A = [5, 8, 2, 22, 12, 9, 3, 57, 25, 84, 2, 3, 8]
hoar_sorting(A)
print(A)

B = ['r', 'g', 'abc', 'rt', 'd', 'vb', 'q', 'a', 'x', 'ui']
hoar_sorting(B)
print(B)