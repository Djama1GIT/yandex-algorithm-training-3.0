def longest_common_subsequence(text1, text2) -> int:
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for idx1, sym1 in enumerate(text1):
        for idx2, sym2 in enumerate(text2):
            if sym1 == sym2:
                dp[idx1 + 1][idx2 + 1] = dp[idx1][idx2] + 1
            else:
                dp[idx1 + 1][idx2 + 1] = max(dp[idx1][idx2 + 1], dp[idx1 + 1][idx2])

    return dp[len(text1)][len(text2)]


print(longest_common_subsequence(*input("Enter line1 and line2 separated by a space: ").split()))
