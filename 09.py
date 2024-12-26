# Day 09

with open('./09.txt') as my_input:
    disk_map = my_input.read()

def assemble_filesystem(disk_map):
    filesystem = []
    block_id = 0
    for idx, number in enumerate(disk_map):
        for i in range(int(number)):
            if idx % 2:
                filesystem.append('.')
            else:
                filesystem.append(str(block_id))
        if not idx % 2:
            block_id += 1
    return filesystem

# Part 1

filesystem = assemble_filesystem(disk_map)

for idx, data in enumerate(filesystem):
    if idx < len(filesystem) and data == '.':
        while filesystem[-1] == '.':
            filesystem.pop()
        filesystem[idx] = filesystem.pop()

print(sum(idx*int(number) for idx, number in enumerate(filesystem)))

# Part 2

def update_filesystem(block_id, files, free_spaces, filesystem):
    for idx, free_space in enumerate(free_spaces):
        if free_space[0] < files[block_id][0]:
            if len(free_space) >= len(files[block_id]):
                for i in range(len(files[block_id])):
                    filesystem[free_space[i]] = block_id
                    filesystem[files[block_id][i]] = 0
                if len(free_space) == len(files[block_id]):
                    free_spaces.pop(idx)
                else:
                    free_spaces[idx] = free_spaces[idx][len(files[block_id]):]
                return filesystem

filesystem = assemble_filesystem(disk_map)

files = {}
free_spaces = [[]]
for idx, data in enumerate(filesystem):
    if data in files.keys():
        files[data].append(idx)
    elif data != '.':
        files[data] = [idx]
    if data == '.':
        free_spaces[-1].append(idx)
    elif free_spaces[-1]:
        free_spaces.append([])
free_spaces.pop()

for block_id in reversed(range(1, int(filesystem[-1]) + 1)):
    update_filesystem(str(block_id), files, free_spaces, filesystem)

for idx, data in enumerate(filesystem):
    if data == '.':
        filesystem[idx] = 0

print(sum(idx*int(number) for idx, number in enumerate(filesystem)))