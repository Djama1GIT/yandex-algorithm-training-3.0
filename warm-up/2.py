k = int(input())
S = input()
maximum = -1
i = 0
while i < len(S) - k:
    sym = S[i]
    before_window = 1
    while before_window + i < len(S) and S[i+1] == sym:
        before_window += 1
        i += 1
    after_window = 0
    while i + 1 + k + after_window < len(S) and S[i + k + after_window + 1] == sym:
        after_window += 1
    maximum = max(maximum, before_window + k + after_window)
    i += 1
print(maximum)