left, down, right, up = 10**9, 10**9, 0, 0
for i in range(int(input())):
    x, y = map(int, input().split())
    left = min(left, x)
    down = min(down, y)
    right = max(right, x)
    up = max(up, y)
print(left, down, right, up)
