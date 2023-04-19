import bisect

n = int(input())
N = sorted(list(set(map(int, input().split()))))
k = int(input())
p = list(map(int, input().split()))
for i in p:
    print(bisect.bisect_right(N, i))
