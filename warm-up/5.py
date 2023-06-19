res = 0
prev = 0
for _ in range(int(input())):
    now = int(input())
    res += min(prev, now)
    prev = now
print(res)