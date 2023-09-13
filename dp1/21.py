N = int(input())

n = 3 if N < 3 else N
dp = [0] * (3 if N < 3 else N + 1)
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

print(dp[N])
