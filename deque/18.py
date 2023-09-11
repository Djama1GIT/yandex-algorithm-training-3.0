from collections import deque

queue = deque()

while (cmd := input().split())[0] != 'exit':
    match cmd[0]:
        case "push_front":
            queue.appendleft(cmd[1])
            print("ok")
        case "push_back":
            queue.append(cmd[1])
            print("ok")
        case "pop_front":
            if len(queue) == 0:
                print("error")
                continue
            print(queue.popleft())
        case "pop_back":
            if len(queue) == 0:
                print("error")
                continue
            print(queue.pop())
        case "size":
            print(len(queue))
        case "front":
            if len(queue) == 0:
                print("error")
                continue
            print(queue[0])
        case "back":
            if len(queue) == 0:
                print("error")
                continue
            print(queue[-1])
        case "clear":
            queue.clear()
            print("ok")
print("bye")
