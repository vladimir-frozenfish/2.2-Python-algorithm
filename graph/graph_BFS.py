"""
граф - поиск в ширину
BFS - Breadth-First Search
Время выполнения O(V+E) - (V - количество вершин, E - количество ребер)

осуществляем поиск друга (узла), по какому-либо (условному) признаку
"""

from collections import deque


def person_is_seller(person):
    """функция возвращает True, если имя друга оканчивается на '_m'
    """
    return True if person[-2:] == '_m' else False


def search_path(graph, searched, person):
    """восстановление пути от найденного друга до 'me'
    """
    if not searched:                                        # если список searched пуст изначально, то найденный друг (узел) непосредственно соседствует с 'me'
        return ['me'] + [person]

    path = []                                               # массив для пути
    connecting_person = person                              # промежуточный друг (узел)

    while searched:                                         # пока список персон не пуст
        previous_person = searched.pop()                    # предудыщий друг (узел) из очереди
        if connecting_person in graph['me']:                # если промежуточный друг находится в связи с 'me'
            path.append(connecting_person)
            break
        if connecting_person in graph[previous_person]:     # если промежуточный друг находится в связи с другом из очереди
            path.append(connecting_person)
            connecting_person = previous_person

    return ['me'] + path[::-1]


def search_BFS(graph: dict):
    """функция осуществляет поиск друга (узла) в графе в ширину
    """

    search_queue = deque()                      # очередь поиска
    search_queue += graph['me']                 # поиск начинается от друзей начального узла - 'me'

    searched = []                               # список проверенных друзей, чтобы не возникало двойных проверок и бесконечного цикла проверки

    while search_queue:                                                                             # пока очередь не пуста
        person = search_queue.popleft()                                                             # из очереди извлекается первый человек
        if not person in searched:                                                                  # если друг не проверядся ранее, то он проходит проверку на определенный признак
            if person_is_seller(person):                                                            # проверяем друга (узел графа) на определенный признак
                return (f'Найден друг, по указанным признакам - это {person} \n'
                        f'Путь до указанного друга - {search_path(graph, searched, person)}')       # восстановление пути от найденного узда до 'me'
            search_queue += graph[person]                                                           # если проверенный друг не подходит, то добавляем в очередь всех его друзей
            searched.append(person)                                                                 # также проверенного друга добавляем в список проверенных

    return f'Друга, по указанным признакам не найдено'


graph = {
    'me': ['vasya', 'alisa', 'petya'],
    'petya': ['masha', 'kolya'],
    'alisa': ['masha', 'nina'],
    'vasya': ['galya'],
    'masha': ['mark_m'],
    'kolya': [],
    'galya': [],
    'nina': [],
    'mark_m': [],
}

print(search_BFS(graph))
