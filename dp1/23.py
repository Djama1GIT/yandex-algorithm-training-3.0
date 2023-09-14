N = int(input())

dp = [0] * (N + 1)
dp_prev = [0] * (N + 1)
for i in range(1, N + 1):
    minimum = dp[i - 1]
    minimum_prev = i - 1
    if i % 2 == 0:
        if dp[i // 2] < dp[i - 1]:
            minimum = dp[i // 2]
            minimum_prev = i // 2
    if i % 3 == 0:
        if i % 2 == 0 and (dp[i // 3] < dp[i // 2]) or (dp[i // 3] < dp[i - 1]):
            minimum = dp[i // 3]
            minimum_prev = i // 3
    dp[i] = minimum + 1
    dp_prev[i] = minimum_prev


recovery = [N]
i = N
while recovery[-1] != 1:
    i = dp_prev[i]
    recovery += [i]

print(len(recovery) - 1)
print(*list(reversed(recovery)))
