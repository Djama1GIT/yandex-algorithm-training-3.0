N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
prefix_matrix = [[0] * (M + 1), *[[0] + matrix[i].copy() for i in range(N)]]
for y in range(2, M + 1):
    prefix_matrix[1][y] = prefix_matrix[1][y - 1] + prefix_matrix[1][y]
for x in range(2, N + 1):
    prefix_matrix[x][1] = prefix_matrix[x - 1][1] + prefix_matrix[x][1]

for y in range(2, N + 1):
    for x in range(2, M + 1):
        prefix_matrix[y][x] = prefix_matrix[y][x] \
                              + prefix_matrix[y][x - 1] \
                              + prefix_matrix[y - 1][x] \
                              - prefix_matrix[y - 1][x - 1]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_matrix[x2][y2] - prefix_matrix[x2][y1 - 1] - prefix_matrix[x1 -1][y2] + prefix_matrix[x1 - 1][
        y1 - 1]
    print(result)
