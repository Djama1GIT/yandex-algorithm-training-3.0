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
        table[n][m] += max(table[n - 1][m], table[n][m - 1])

INF = 99999999999999999999

recovery = []
n, m = N - 1, M - 1
while n > 0 or m > 0:
    if (table[n - 1][m] if n > 0 else -INF) > (table[n][m - 1] if m > 0 else -INF):
        recovery += ["D"]
        n -= 1
    else:
        recovery += ["R"]
        m -= 1

print(table[-1][-1])
print(*reversed(recovery))
