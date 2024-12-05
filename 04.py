# Day 04

with open('./04.txt') as my_input:
    puzzle = my_input.read().splitlines()

# Part 1

puzzle_t = [''.join(line) for line in zip(*puzzle)]

all_diagonals = []
size = len(puzzle)
for i in range(4, size+1):
    diagonals = ['' for _ in range(4)]
    for y, x in ((j, i-j-1) for j in range(i)):
        diagonals[0] += puzzle[y][size-1-x]
        diagonals[1] += puzzle[y][x]
        if i < size:
            diagonals[2] += puzzle[size-1-y][x]
            diagonals[3] += puzzle[size-1-y][size-1-x]
    for diagonal in diagonals:
        all_diagonals.append(diagonal)

counter = 0
for search_area in (puzzle, puzzle_t, all_diagonals):
    for line in search_area:
        counter += line.count('XMAS') + line.count('SAMX')
print(counter)

# Part 2

counter = 0
for y, line in enumerate(puzzle[1:-1], 1):
    for x, char in enumerate(line[1:-1], 1):
        if char == 'A':
            if ''.join(sorted(puzzle[y-1][x-1] + puzzle[y+1][x+1])) == 'MS':
                if ''.join(sorted(puzzle[y-1][x+1] + puzzle[y+1][x-1])) == 'MS':
                    counter += 1
print(counter)


