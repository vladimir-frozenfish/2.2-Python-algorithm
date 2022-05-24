import time

# функия возращает ряд фибоначчи заданного количества и время выполнения функции
def fibonacci_list(i):
    start_func = time.perf_counter()
    if i == 0:
        spisok = [1]
        stop_func = time.perf_counter()
        return (spisok, stop_func - start_func)
    else:
        spisok = [1, 1]
        for summa in range(2, i+1):
            spisok.append(spisok[summa-2]+spisok[summa-1])
        stop_func = time.perf_counter()
        return(spisok, stop_func - start_func)

n = int(input("Введите натуральное число: "))

start = time.perf_counter()

spisok_fibonachi, time_function = fibonacci_list(n)

# print(*spisok_fibonachi, sep="\n") # вывод всего ряда Фибоначчи
print("Последнее число в ряду Фибоначчи:", spisok_fibonachi[n]) # вывод последнего числа в ряду Фибоначчи
stop = time.perf_counter()
print("Время операции функции:", round(time_function, 5), "секунд")
print("Время операции всей программы:", round(stop-start, 5), "секунд")



