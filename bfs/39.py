with open('input.txt', 'r') as file:
    N = int(file.readline())
    blocks = []
    speleologist = ()
    while len(blocks) < N:
        file.readline()
        blocks += [[]]
        for i in range(N):
            layer = file.readline().strip()
            if 'S' in layer:
                speleologist = (len(blocks) - 1, i, layer.index('S'))
                layer = layer.replace('S', '.')
            blocks[-1] += [layer]

# [[print(*i, sep='\n'), print()] for i in blocks]
# print(speleologist)

distances = [[speleologist]]
already_processed_xyz = {
    speleologist: True
}

broken = False
while not broken:
    distances += [[]]
    for spel in distances[-2]:
        y, x, z = spel
        if y > 0 and blocks[y - 1][x][z] == '.':
            if not already_processed_xyz.get((y - 1, x, z)):
                distances[-1] += [(y - 1, x, z)]
                already_processed_xyz[(y - 1, x, z)] = True
        if y + 1 < len(blocks) and blocks[y + 1][x][z] == '.':
            if not already_processed_xyz.get((y + 1, x, z)):
                distances[-1] += [(y + 1, x, z)]
                already_processed_xyz[(y + 1, x, z)] = True
        if x > 0 and blocks[y][x - 1][z] == '.':
            if not already_processed_xyz.get((y, x - 1, z)):
                distances[-1] += [(y, x - 1, z)]
                already_processed_xyz[(y, x - 1, z)] = True
        if x + 1 < len(blocks[y]) and blocks[y][x + 1][z] == '.':
            if not already_processed_xyz.get((y, x + 1, z)):
                distances[-1] += [(y, x + 1, z)]
                already_processed_xyz[(y, x + 1, z)] = True
        if z > 0 and blocks[y][x][z - 1] == '.':
            if not already_processed_xyz.get((y, x, z - 1)):
                distances[-1] += [(y, x, z - 1)]
                already_processed_xyz[(y, x, z - 1)] = True
        if z + 1 < len(blocks[y][x]) and blocks[y][x][z + 1] == '.':
            if not already_processed_xyz.get((y, x, z + 1)):
                distances[-1] += [(y, x, z + 1)]
                already_processed_xyz[(y, x, z + 1)] = True

    for i in distances[-1]:
        if i[0] == 0:
            print(len(distances) - 1)
            broken = True
            break
