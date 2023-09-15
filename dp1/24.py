N = int(input())
A = [float('inf')] * 3 + [0] * N
B = [float('inf')] * 3 + [0] * N
C = [float('inf')] * 3 + [0] * N
for i in range(3, N + 3):
    A[i], B[i], C[i] = map(int, input().split())

dp = [0] * (N + 3)

for i in range(3, N + 3):
    dp[i] = min([
        dp[i - 1] + A[i],
        dp[i - 2] + B[i - 1],
        dp[i - 3] + C[i - 2],
    ])

# [print(A[i], B[i], C[i], dp[i]) for i in range(N + 3)]
print(dp[-1])