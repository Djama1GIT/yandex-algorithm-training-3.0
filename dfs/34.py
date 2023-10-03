from collections import deque


def topological_sort(graph, num) -> list[int]:
    degree = {vtx: 0 for vtx in range(1, num + 1)}
    for vtx in graph:
        for vertx in graph[vtx]:
            degree[vertx] += 1

    queue = deque([idx for idx in range(1, num + 1) if degree[idx] == 0])
    answer = []

    while queue:
        vtx = queue.popleft()
        answer.append(vtx)
        if vtx in graph:
            for vertx in graph[vtx]:
                degree[vertx] -= 1
                if degree[vertx] == 0:
                    queue.append(vertx)
    return answer


N, M = map(int, input().split())
m = [tuple(map(int, input().split())) for _ in range(M)]

vertexes = {}

for vertex in m:
    if not vertex[0] in vertexes:
        vertexes[vertex[0]] = []
    if not vertex[1] in vertexes:
        vertexes[vertex[1]] = []

    vertexes[vertex[0]] += [vertex[1]]

result = topological_sort(vertexes, N)
if len(result) == N:
    print(*result)
else:
    print(-1)
