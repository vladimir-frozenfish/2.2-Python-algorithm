life_program = True

''' 
функции кодировки и раскодировки строки с заданным сдвигом. 
Если сдвиг строки выходит за длину алфавита, то сдвиг возвращается в начало алфавита в кодировке.
В раскодировке наоборот в конец алфавита

В новой версии это делается одной строкой вычисления, путем нахождения остатка от деления итогового сдвига на длину алфавита
'''


def coding(stroka_input):
    stroka_output = ''

    for i in stroka_input:
        # проверка вхождения символа в кодируемый алфавит
        if i in alphabet:
            stroka_output += alphabet[(alphabet.index(i) + sdvig) % len(alphabet)]
            '''
            if alphabet.index(i) + sdvig < len(alphabet):
                stroka_output += alphabet[alphabet.index(i) + sdvig]
            else:
                stroka_output += alphabet[alphabet.index(i) + sdvig - len(alphabet)]
            '''
        # если символ не входит в алфавит, то он остается не кодируемым
        else:
            stroka_output += i

    return stroka_output


def encoding(stroka_input):
    stroka_output = ''

    for i in stroka_input:
        # проверка вхождения символа в кодируемый алфавит
        if i in alphabet:
            stroka_output += alphabet[(alphabet.index(i) - sdvig) % len(alphabet)]
            '''
            if alphabet.index(i) - sdvig >= 0:
                stroka_output += alphabet[alphabet.index(i) - sdvig]
            else:
                stroka_output += alphabet[alphabet.index(i) - sdvig + len(alphabet)]
            '''
        # если символ не входит в алфавит, то он остается не кодируемым
        else:
            stroka_output += i

    return stroka_output


# список кодируемых символов
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
            'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
            'ъ', 'ы', 'ь', 'э', 'ю', 'я',
            'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З',
            'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
            'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
            'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
            ' ', '!', '.', ',', '?']
# шаг сдвига
sdvig = 5

while life_program:
    print('1) Закодировать строку')
    print('2) Декодировать строку')
    print('3) Выйти из программы')
    deystvie = int(input('Выберите действие: '))

    if deystvie == 3:
        life_program = False

    elif deystvie == 1:
        stroka_input = input('Введите строку для кодирования: ')
        print(coding(stroka_input))

    elif deystvie == 2:
        stroka_input = input('Введите строку для декодирования: ')
        print(encoding(stroka_input))

    else:
        print('Введите правильно номер действия.')
