N = int(input())  # rows
n_rows_ints = list(map(int, input().split()))
M = int(input())  # columns
m_columns_ints = list(map(int, input().split()))

table = [[0] * (M + 1) for i in range(N + 1)]

for column_idx in range(1, M + 1):
    for row_idx in range(1, N + 1):
        if n_rows_ints[row_idx - 1] == m_columns_ints[column_idx - 1]:
            table[row_idx][column_idx] = table[row_idx - 1][column_idx - 1] + 1
        else:
            table[row_idx][column_idx] = max(table[row_idx][column_idx - 1], table[row_idx - 1][column_idx])

column_idx, row_idx = M, N
recovery = []
max_column = M
rec_len = table[-1][-1]
while row_idx > 0 and rec_len > 0:
    if column_idx <= 0:
        column_idx = max_column
        row_idx -= 1
    if n_rows_ints[row_idx - 1] == m_columns_ints[column_idx - 1] and table[row_idx][column_idx] == rec_len:
        recovery.append(m_columns_ints[column_idx - 1])
        column_idx -= 1
        row_idx -= 1
        rec_len -= 1
        max_column = column_idx
    else:
        column_idx -= 1

print(*list(reversed(recovery)))
