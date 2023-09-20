N, M = map(int, input().split())

table = [[0] * M for _ in range(N)]

for n in range(N):
    table[n] = list(map(int, input().split()))

for m in range(1, M):
    table[0][m] += table[0][m - 1]

for n in range(1, N):
    table[n][0] += table[n - 1][0]

for n in range(1, N):
    for m in range(1, M):
        table[n][m] += min(table[n - 1][m], table[n][m - 1])

# [print(*row, sep='\t') for row in table]

print(table[-1][-1])
