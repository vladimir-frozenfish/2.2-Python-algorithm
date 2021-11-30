"""
Считывание списка ребер в матрицу смежности и список смежности
Компактное хранение списков смежности для неизменяемого графа
"""
def getting_adjacency_matrix_v2():
    """
    INPUT
    N - vertices
    M - edges
    |N M|
    -----
    graph
    -----
    |A B|
    |B C|
    |B D|

    """
    N, M = [int(x) for x in input().split()]
    V = []
    index = dict()
    count_vertices = 0  # определение индекса вершин
    A = [[0] * N for _ in range(N)]
    for i in range(M):
        v1, v2 = input().split()
        V.append([v1, v2])  # сохраняем ребра
        for v in v1, v2:
            if v not in index:
                count_vertices += 1
                index[v] = count_vertices - 1
    for v1, v2 in V:  # получение матрицы смежности
        v1_i = index[v1]
        v2_i = index[v2]
        A[v1_i][v2_i] = 1  # для ориентированного графа
        A[v2_i][v1_i] = 1  # добавить для неориентированного графа
    print(A)
    print(index)
    print(V)


"""
Считывание списка ребер в список смежности
"""
def getting_adjacency_list():
    N, M = [int(x) for x in input('Введите количество вершин и ребер графа (через пробел): ').split()]
    G = {}

    for i in range(M):
        v1, v2 = input(f'Введите ребро {i+1}: ').split()
        for v, u in (v1, v2), (v2, v1):
            if v not in G:
                G[v] = {u}
            else:
                G[v].add(u)

    print(G)



# getting_adjacency_matrix_v2()
getting_adjacency_list()