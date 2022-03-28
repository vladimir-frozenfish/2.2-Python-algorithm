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



'''
srt_len = 10
str_random = (
        random.choice(string.ascii_uppercase)
        + ''.join([random.choice(string.ascii_lowercase) for i in range(srt_len)])
)
print(str_random)

list_len = 10
list_random = [(
        random.choice(string.ascii_uppercase)
        + ''.join([random.choice(string.ascii_lowercase) for i in range(srt_len)])
) for j in range(list_len)]
print(sorted(list_random))
'''


