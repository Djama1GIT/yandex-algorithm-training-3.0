def solve(n, coordinates):
    coordinates.sort()
    dp = [0] * n
    dp[0] = 0
    dp[1] = coordinates[1] - coordinates[0]

    for i in range(2, n):
        dp[i] = coordinates[i] - coordinates[i - 1] + dp[i - 1]
        for j in range(1, i - 1):
            dp[i] = min(dp[i], dp[j] + coordinates[i] - coordinates[j + 1])

    return dp[n - 1]


print(solve(int(input()), list(map(int, input().split()))))
