M = int(input())
N = int(input())
sections = [[*map(int, input().split()), 1] for i in range(N)]
count = len(sections)
for i in range(1, len(sections)):
    for j in range(i):
        if sections[j][2] == 0:
            continue
        if sections[i][0] <= sections[j][1] and sections[i][1] >= sections[j][0]:
            count -= 1
            sections[j][2] = 0
print(count)