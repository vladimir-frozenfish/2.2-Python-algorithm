#  функция возращает факториал числа
def factorial(i):
    if i == 0:
        return 1
    else:
        fact = 1
        for counter in range(1, i + 1):
            fact *= counter
        return fact

# рекурсивная функция возращает факториал числа
def factorial_recur(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        return i * factorial_recur(i - 1)

n = int(input("Введите натуральное число: "))

print("Факториал числа", n, "=", factorial(n))

# print("Рекурсия Факториал числа", n, "=", factorial_recur(n))