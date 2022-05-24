import string
import random


def random_string(len, symbols=string.ascii_letters):
    """функция возвращает случайную строку, заданной длинны из заданных символов,
    если символы не заданы, то по умолчанию, это заглавные и прописные латинские буквы"""
    return ''.join([random.choice(symbols) for i in range(len)])


def random_string_list(len_list, len_string=10, symbols=string.ascii_letters):
    """функция возвращает спиок заданной длинны из случайных строк, заданной длинны (или по умолчанию равной 10)
    из заданных символов, если символы не заданы, то по умолчанию, это заглавные и прописные латинские буквы"""
    return [random_string(len_string, symbols) for i in range(len_list)]

if __name__ == '__main__':
    print(random_string(20))
    print(random_string_list(5, 6, 'abcdefg12345'))