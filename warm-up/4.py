n = int(input())
k = int(input())
row = int(input())
left_or_right = int(input())

if k == n:
    print(-1)
else:
    desks = list(range(n))
    desks = [desk % k + 1 for desk in desks]
    variant = (row - 1) * 2 + left_or_right - 1
    i = 0
    while variant - i >= 0 or variant + i < len(desks):
        i += 1
        solves = []
        if len(desks) > variant + i and desks[variant + i] == desks[variant]:
            solves += [variant + i]
        if variant - i >= 0 and desks[variant - i] == desks[variant]:
            solves += [variant - i]
        if len(solves) >= 1:
            if len(solves) == 2 and solves[0] // 2 > solves[1] // 2:
                print(solves[1] // 2 + 1, solves[1] % 2 + 1)
            else:
                print(solves[0] // 2 + 1, solves[0] % 2 + 1)
            break
    else:
        print(-1)




