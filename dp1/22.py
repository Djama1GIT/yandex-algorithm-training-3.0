N, k = map(int, input().split())

dp = [1] + [0] * (N - 1)
for i in range(1, N):
    dp[i] = sum(dp[max(0, i-k):i])

print(dp[-1])
