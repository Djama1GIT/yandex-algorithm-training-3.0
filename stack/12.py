stck = input()
_stack = []
pairs = {
    '{': '}',
    '[': ']',
    '(': ')',
}
for i in stck:
    if i in pairs.keys():
        _stack += [i]
    else:
        if len(_stack) and i == pairs[_stack[-1]]:
            del _stack[-1]
        else:
            print('no')
            break
else:
    print('yes' if len(_stack) == 0 else 'no')

