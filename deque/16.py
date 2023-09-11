from collections import deque

queue = deque()

while (cmd := input().split())[0] != 'exit':
    match cmd[0]:
        case "push":
            queue.append(cmd[1])
            print("ok")
        case "size":
            print(len(queue))
        case "pop":
            if len(queue) == 0:
                print("error")
                continue
            print(queue.popleft())
        case "front":
            if len(queue) == 0:
                print("error")
                continue
            print(queue[0])
        case "clear":
            queue.clear()
            print("ok")
print("bye")
