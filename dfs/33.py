yes_or_no = True


def dfs(graph, visited, now, flag):
    global yes_or_no
    if not yes_or_no:
        return
    visited[now] = flag
    for idx, vertex in enumerate(graph[now]):
        if visited.get(vertex, None) is None:
            dfs(graph, visited, vertex, not flag)
        elif visited.get(vertex, None) == flag:
            yes_or_no = False
            return


N, M = map(int, input().split())
m = [tuple(map(int, input().split())) for _ in range(M)]
vertexes = {}
is_visited = {}

for i in range(1, N + 1):
    vertexes[i] = []
    is_visited[i] = None

for edge in m:
    vertexes[edge[0]] += [edge[1]]
    vertexes[edge[1]] += [edge[0]]

if N > 0 and M > 0:
    for vtx in vertexes:
        if not is_visited[vtx]:
            dfs(vertexes, is_visited, vtx, False)
print("YES" if yes_or_no else "NO")
