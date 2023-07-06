from collections import deque

stck = deque()

for i in input().strip().split():
    if i.isnumeric():
        stck.append(int(i))
    if i == '+':
        stck.append(stck.pop() + stck.pop())
    elif i == '-':
        temp = stck.pop()
        stck.append(stck.pop() - temp)
    elif i == '*':
        stck.append(stck.pop() * stck.pop())
print(stck[0])
