n = int(input())
N = list(map(int, input().split()))
result = [-1] * n

stck = []
for i, v in enumerate(N):
    while stck and stck[-1][1] > v:
        result[stck[-1][0]] = i
        del stck[-1]
    if not stck or stck[-1][1] <= v:
        stck += [(i, v)]
print(*result)


