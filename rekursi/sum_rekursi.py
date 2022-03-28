def sum_rekursi(arr):
    """рекурсиваная функция, вовзращает сумму чисел в списке"""
    return 0 if not arr else arr.pop() + sum_rekursi(arr)

def count_rekursi(arr):
    """рекурсивная функция, возвращает длинну списка"""
    if not arr:
        return 0
    arr.pop()
    return 1 + count_rekursi(arr)


arr = [1, 2, 3, 4, 5, -4]
print(sum_rekursi(arr))


arr = [1, 2, 3, 4, 5, -4]
print(count_rekursi(arr))