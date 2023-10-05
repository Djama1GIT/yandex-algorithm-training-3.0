def get_way(matrix: list[tuple[int]], start: int, end: int) -> int:
    visited = [[start - 1]]
    counter = 0
    still_not_found = [i for i in range(len(matrix))]
    len_snf = len(still_not_found)

    while (end - 1) not in visited[-1]:
        visited += [[]]
        counter += 1
        for i in visited[-2]:
            if not still_not_found:
                break
            idx = still_not_found[0]
            while -1 < idx <= still_not_found[-1]:
                _idx = -1
                if still_not_found.index(idx) < len(still_not_found) - 1:
                    _idx = still_not_found[still_not_found.index(idx) + 1]
                if matrix[i][idx] and (idx not in visited[-1]) and (idx in still_not_found):
                    visited[-1] += [idx]
                    del still_not_found[still_not_found.index(idx)]
                idx = _idx
        if len_snf == len(still_not_found) and (end - 1) not in visited[-1]:
            return -1
        else:
            len_snf = len(still_not_found)
        del visited[0]
    return counter


with open('input.txt', 'r') as file:
    N = int(file.readline())
    m = [tuple(map(int, file.readline().split())) for _ in range(N)]
    s, e = map(int, file.readline().split())

print(get_way(m, s, e))
