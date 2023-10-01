import sys

sys.setrecursionlimit(2147000000)


def dfs(graph: dict[int, list[int]], visited: dict[int, bool], now: int, comp: list[list[int]], comp_n: int):
    visited[now] = True
    comp[comp_n] += [now]
    for edg in graph[now]:
        if not visited[edg]:
            dfs(graph, visited, edg, comp, comp_n)


N, M = map(int, input().split())
m = [tuple(map(int, input().split())) for _ in range(M)]
vertexes = {}
is_visited = {}

for i in range(1, N + 1):
    vertexes[i] = []
    is_visited[i] = False

for edge in m:
    vertexes[edge[0]] += [edge[1]]
    vertexes[edge[1]] += [edge[0]]

if N == 0:
    print(0)
else:
    comps = [[]]
    comp_num = 0
    for vertex in vertexes:
        if not is_visited[vertex]:
            dfs(vertexes, is_visited, vertex, comps, comp_num)
            comps += [[]]
            comp_num += 1
    print(len(comps) - 1)
    for i in reversed(sorted(comps, key=lambda x: len(x))):
        if i:
            print(len(i))
            print(*sorted(i))
