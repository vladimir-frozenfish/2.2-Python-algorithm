"""выделение компонента связности графа"""


def dfs(vertex, G):

    used.add(vertex)

    for neighborn in G[vertex]:
        if neighborn not in used:
            dfs(neighborn, G, used)

G = {}
used = {}
N = 0
for vertex in G:
    if vertex not in used:
        dfs(vertex, G)
        N += 1
