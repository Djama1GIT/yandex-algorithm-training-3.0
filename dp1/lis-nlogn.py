from bisect import bisect_left

lst = [10, 22, 9, 33, 21, 50, 41, 60, 80]


def lis(lst_):
    tail = [float('inf')] * len(lst_)
    # [inf, inf, inf, inf, inf, inf, inf, inf, inf, ]
    tail[0] = lst_[0]
    # [10, inf, inf, inf, inf, inf, inf, inf, inf, ]
    # [10, 22, inf, inf, inf, inf, inf, inf, inf, ]
    # [9, 22, inf, inf, inf, inf, inf, inf, inf, ]
    # [9, 22, 33, inf, inf, inf, inf, inf, inf, ]
    # [9, 21, 33, inf, inf, inf, inf, inf, inf, ]
    # [9, 21, 33, 50, inf, inf, inf, inf, inf, ]
    # [9, 21, 33, 41, inf, inf, inf, inf, inf, ]
    # [9, 21, 33, 41, 60, inf, inf, inf, inf, ]
    # [9, 21, 33, 41, 60, 80, inf, inf, inf, ]
    for x in lst_[1:]:
        if x > tail[-1]:
            tail[bisect_left(tail, float('inf'))] = x
        else:
            tail[bisect_left(tail, x)] = x

    return bisect_left(tail, float('inf'))


print(lis(lst))  # Output: 6


# С восстановлением ответа
def lis(lst_):
    tail = [0] * len(lst_)
    prev = [-1] * len(lst_)

    length = 1
    for i in range(1, len(lst_)):
        if lst_[i] > lst_[tail[length - 1]]:
            prev[i] = tail[length - 1]
            tail[length] = i
            length += 1
        else:
            pos = bisect_left([lst_[tail[j]] for j in range(length)], lst_[i])
            prev[i] = tail[pos - 1] if pos else -1
            tail[pos] = i

    i = tail[length - 1]
    result = []
    while i >= 0:
        result.append(lst_[i])
        i = prev[i]
    result.reverse()

    return result


lst = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(lst))
