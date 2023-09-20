N, M = map(int, input().split())

table = [[0] * (M + 2) for _ in range(N + 2)]

table[2][2] = 1

for n in range(2, N + 2):
    for m in range(2, M + 2):
        table[n][m] += table[n - 2][m - 1] + table[n - 1][m - 2]

# [print(*row[2:], sep='\t') for row in table[2:]]

print(table[-1][-1])
