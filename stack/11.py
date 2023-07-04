stck = []
while (cmd := input().split())[0] != 'exit':
    match cmd[0]:
        case 'push':
            stck += [cmd[1]]
            print('ok')
        case 'pop':
            print(stck.pop() if len(stck) else 'error')
        case 'back':
            print(stck[-1] if len(stck) else 'error')
        case 'size':
            print(len(stck))
        case 'clear':
            stck = []
            print('ok')
print('bye')

