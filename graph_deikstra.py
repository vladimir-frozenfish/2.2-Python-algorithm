from collections import deque


def main():
    """считываем граф"""
    # G = read_graph()
    G = {'a': {'b': 2.0, 'd': 4.0, 'c': 5.0},
         'b': {'a': 2.0, 'c': 1.0},
         'd': {'a': 4.0, 'e': 7.0},
         'c': {'b': 1.0, 'e': 1.0, 'a': 5.0},
         'e': {'c': 1.0, 'd': 7.0}}
    print(G)

    start = input('С какой вершины начать? - ')
    while start not in G:
        start = input('Такой вершиины нет на графе. \n '
                      'С какой вершины начать? - ')

    shortest_distances = dijkstra(G, start)
    print(shortest_distances)


    finish = input('К какой вершине построить путь? - ')
    while finish not in G:
        finish = input('Такой вершиины нет на графе. \n '
                       'К какой вершине построить путь? - ')

    shortest_path = reveal_shortest_path(G, start, finish, shortest_distances)
    print(shortest_path)


def read_graph():
    """считываем данные о графе и заносим в словарь"""
    M = int(input('Введите количество ребер M: '))
    G = {}

    for i in range(M):
        print('Введите вершины ребра и вес ребра:')
        a, b, weight = input().split()
        weight = float(weight)

        """добавление ребёр в графе"""
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G


def dijkstra(G, start):
    """алгоритм Дейкстры - поиск кратчайших путей
    от стртовой вершины до всех вершин"""
    Q = deque()
    """словарь кратчайших расстояний"""
    S = {}
    S[start] = 0
    Q.append(start)

    while Q:
        v = Q.popleft()
        for u in G[v]:
            if (u not in S) or (S[v]+G[v][u] < S[u]):
                S[u] = S[v] + G[v][u]
                Q.append(u)

    return S


def reveal_shortest_path(G, start, finish, shortest_distances):
    """восстановление кратчайшего пути от стратовой точки до указанной"""
    Q = deque()
    v = finish
    """добавляем в очередь последнюю вершину"""
    Q.append(v)

    while v is not start:
        """
        вычисляем для каждой из её соседей,
        совпадает ли сумма (кратч.расст. соседки + величина
        ребра) с кратч.расст. текущей вершины. Если да, то
        соседка принадлежит одному из кратч.путей.
        Все кратч.пути искать не нужно, поэтому выходим из цикла
        и продолжаем операции уже с соседней вершиной.
        """
        for n in G[v]:
            if shortest_distances[v] == shortest_distances[n] + G[v][n]:
                Q.appendleft(n)
                v = n
                break
    return list(Q)


def add_edge(G, a, b, weight):
    """добавление ребра в граф"""
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight


if __name__ == '__main__':
    main()