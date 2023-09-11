from collections import deque

first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

cnt = 0

while len(first) != 0 and len(second) != 0:
    first_card = first.popleft()
    second_card = second.popleft()
    queue = first if (first_card == 0 and second_card == 9) else \
        second if (second_card == 0 and first_card == 9) else \
        first if first_card > second_card else second
    (queue).append(first_card)
    (queue).append(second_card)
    cnt += 1

    if cnt > 10**6:
        print("botva")
        break
else:
    print("first" if len(second) == 0 else "second", cnt)
