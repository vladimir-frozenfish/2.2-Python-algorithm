# не работает - выдает ошибку - из книги Грокаем алгоритмы
"""
алгоритм Дейкстры - поиск кратчайшего пути (учитывая стоимость)
от пункта start до finish в графе
граф - направленный ацикличный граф (DAG - Directed Acyclic Graph)
"""


def find_lowes_cost_node(costs, processed):
    """
    функция возвращает узел с наименьшей стоимостью
    """
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def deikstra_start_finish(graph: dict):

    infinity = float('inf')
    """словарь первоначальных стоимостей от Start до 
    известных пунктов, плюс до Finish - бесконечность
    """
    costs = {}
    costs.update(graph['Start'])
    costs['Finish'] = infinity

    """словарь первоначальных родителей для соседей Start и для Finish"""
    parents = {}
    for i in graph['Start'].keys():
        parents[i] = 'Start'
    parents['Finish'] = None

    """массив для отслеживания обработанных узлов,
    чтобы один узел не обрабатывался многократно"""
    processed = []

    node = find_lowes_cost_node(costs, processed)                   # найти узел с наиеньшей стоимостью среди необработанных
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            print(n)
            print(costs)
            print(costs[n])
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowes_cost_node(costs, processed)

    return costs


graph = {
    'Start': {'a': 5, 'c': 2},
    'a': {'b': 4, 'c': 3},
    'b': {'Finish': 10},
    'c': {'e': 5},
    'e': {'b': 1, 'Finish': 20},
    'Finish': {},
}

print(deikstra_start_finish(graph))


