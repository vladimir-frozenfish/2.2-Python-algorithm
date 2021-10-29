# реверс строки с определенного элемента
# c - 3 элемента Исходня строка - 123456, перевернутая 123654
'''
n = 3
stroka = '123456789'
stroka_tmp = stroka[n::]
stroka_reverse = stroka[0:n] + stroka_tmp[::-1]

print(stroka_reverse)

'''

# реверсируем список от определенного элемента
n = 6
spisok = [1,2,3,4,5,6,7,8]

spisok_reverse = spisok[0: n+1] + spisok [-1: n: -1]
print(spisok_reverse)

stroka = '123abc'
stroka_reverse = stroka[0:3] + stroka[-1 : 2 : -1]
print(stroka_reverse)