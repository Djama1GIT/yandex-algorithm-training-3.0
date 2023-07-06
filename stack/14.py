n = int(input())
N = list(map(int, input().split()))
top = 0
stck = []
for i in N:
    stck += [i]
    while stck and stck[-1] == top + 1:
        top = stck.pop()
print('NO' if stck else 'YES')
