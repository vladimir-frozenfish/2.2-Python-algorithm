def fibonacci_rekursive(n):
    if n == 1 or n == 0:
        return 1
    return fibonacci_rekursive(n-1) + fibonacci_rekursive(n-2)

print(fibonacci_rekursive(40))