N, M, S, T, Q = map(int, input().split())
fleas = {tuple(map(int, input().split())) for _ in range(Q)}

visited = {
    (S, T): 0,
}

horse = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
]

distances = [[(S, T)]]

while distances[-1]:
    distances += [[]]
    for x, y in distances[-2]:
        for x_move, y_move in horse:
            if 0 < x + x_move <= N and 0 < y + y_move <= M:
                xy = (x + x_move, y + y_move)
                if xy not in visited:
                    visited[xy] = len(distances) - 1
                    distances[-1] += [xy]

if not len(fleas - set(visited)):
    summ = 0
    for flea in visited:
        if flea in fleas:
            summ += visited[flea]
    print(summ)
else:
    print(-1)