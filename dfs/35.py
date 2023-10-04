def dfs(count_of_vertexes: int, graph: dict[int, list[int]]) -> list[int]:
    recovery = []
    cycle = False
    visited = {vertex: None for vertex in range(1, count_of_vertexes + 1)}

    def _dfs(now, prev):
        nonlocal recovery, cycle
        if cycle:
            return recovery
        visited[now] = False
        for vertex in graph[now]:
            if vertex != prev:
                if visited.get(vertex, None) is None:
                    _dfs(vertex, now)
                elif visited.get(vertex, None) is False:
                    cycle = True
                    if not recovery:
                        recovery += [vertex]

        visited[now] = True
        if recovery:
            recovery += [now]

    for vertex in graph:
        if visited.get(vertex, None) is None:
            cycle = False
            _dfs(vertex, -1)

    return recovery


with open('input.txt', 'r') as file:
    n = int(file.readline())
    vertexes = {}
    for i in range(n):
        row = list(map(int, file.readline().split()))
        vertexes[i + 1] = []
        for idx, j in enumerate(row):
            if j:
                vertexes[i + 1] += [idx + 1]

answer = dfs(n, vertexes)
if answer:
    print("YES")
    answer = answer[1:answer[1:].index(answer[0]) + 2]
    print(len(answer))
    print(*answer)
else:
    print("NO")
