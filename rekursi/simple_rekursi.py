def minus(number):
    if number == -1:
        return None
    print(number)
    number -= 1
    minus(number)


minus(100)