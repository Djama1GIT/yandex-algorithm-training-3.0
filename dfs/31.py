import sys

sys.setrecursionlimit(2147000000)


def dfs(graph: dict[int, list[int]], visited: dict[int, bool], now: int):
    visited[now] = True
    for i in graph[now]:
        if not visited.get(i, False):
            dfs(graph, visited, i)


N, M = map(int, input().split())
m = [tuple(map(int, input().split())) for _ in range(M)]
vertexes = {}
is_visited = {}
for edge in m:
    if edge[0] not in vertexes:
        vertexes[edge[0]] = []
    if edge[1] not in vertexes:
        vertexes[edge[1]] = []
    vertexes[edge[0]] += [edge[1]]
    vertexes[edge[1]] += [edge[0]]
    is_visited[edge[0]] = False
    is_visited[edge[1]] = False
if N == 0:
    print(0)
elif M == 0:
    print(1)
    print(1)
else:
    vertex = 1
    if vertex not in vertexes:
        print(1)
        print(1)
    else:
        dfs(vertexes, is_visited, vertex)
        print(sum(is_visited.values()))
        print(*sorted([k for k, _v in is_visited.items() if _v]))
