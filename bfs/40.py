from collections import defaultdict


def bfs(graph, start, end):
    visited = set()
    queue = [(start, 0)]

    while queue:
        station, transfers = queue.pop(0)
        if station == end:
            return transfers - 1
        if station not in visited:
            visited.add(station)
            for next_station in graph[station]:
                queue.append((next_station, transfers + 1))
    return -1


N = int(input())
M = int(input())
graph = defaultdict(list)

for i in range(M):
    line = list(map(int, input().split()))[1:]
    for j in range(len(line)):
        for k in range(j + 1, len(line)):
            graph[line[j]].append(line[k])
            graph[line[k]].append(line[j])

A, B = map(int, input().split())
print(bfs(graph, A, B))
