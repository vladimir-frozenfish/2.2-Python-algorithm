'''
Генерация перестановок алгоритмом Найараны
лексикографическая перестановка
'''

def find_elements(string_temp:str, comparison_list:list):
    '''
    функция поиска элементов по алгоритму Найараны.
    возвращает два индекса элементов во временной строке в списке, которые необходимо поменять местами
    если таких элементов нет, возвращает пустой список
    '''
    string_temp = list(string_temp)
    x = []

    # с конца строки (с предпоследнего элемента) осуществляется поиск индекса элемента,
    # для элемента который меньше следующего за собой
    for i in range(len(string_temp)-2, -1, -1):
        # вес текущего эелемнта и вес следующего за ним элемента
        weight_current = comparison_list.index(string_temp[i])+1
        weight_next = comparison_list.index(string_temp[i+1])+1

        if weight_current < weight_next:
            x.append(i)
            break

    # осуществляется поиск с конца строки индекса элемента вес которого больше веса найденного на предыдущем цикле
    if x != []:
        for i in range(len(string_temp)-1, -1, -1):
            weight_i = comparison_list.index(string_temp[i])+1
            if weight_i > weight_current:
                x.append(i)
                break

    return x


def genereate_permutations_nayaran(string_for_permutations:str):
    # строка помещаяетс в список поэлементо для последующего сравнения символов,
    # где индекс в это списке будет соответствовать "весу" символа
    comparison_list = list(string_for_permutations)

    # в список помещается первая исходная строка также во временную список помещается исходная строка
    # для осуществления перестановок
    permutations_list = [string_for_permutations]
    string_temp = string_for_permutations

    x = find_elements(string_temp, comparison_list)
    while x != []:
        # замена элементов по найденным в функции индексам,
        # элементы от первого найденного реверсируются и
        # помещение измененной строки в список перестановок
        string_temp = list(string_temp)
        first_element = x[0]
        second_element = x[1]

        string_temp[first_element], string_temp[second_element] = string_temp[second_element], string_temp[first_element]
        string_temp = string_temp[0: x[0]+1] + string_temp[-1: x[0]: -1]

        string_temp = ''.join(string_temp)
        permutations_list.append(string_temp)

        x = find_elements(string_temp, comparison_list)

    return permutations_list


string_start = input('Введите строку для генерации перестановок: ')

string_permutations = genereate_permutations_nayaran(string_start)
#print('Варианты перестановок:', string_permutations)
print('Количество перестановок:', len(string_permutations))
