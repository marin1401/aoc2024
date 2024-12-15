# Day 06

with open('./06.txt') as my_input:
    area = my_input.read().splitlines()

area = [[column for column in row] for row in area]

def in_area(y, x, area):
    return y >= 0 and x >= 0 and y < len(area) and x < len(area)

def get_path(position , heading, area):
    locations = set()
    locations_and_headings = set()
    while True:
        y, x = position
        if (y, x, heading) in locations_and_headings:
            return False
        locations.add((y, x))
        locations_and_headings.add((y, x, heading))
        if heading == '^':
            if not in_area(y-1, x, area):
                return locations
            if area[y-1][x] != '#':
                position = (y-1, x)
            elif area[y][x+1] != '#':
                position = (y, x+1)
                heading = '>'
            else:
                heading = 'v'
        elif heading == '>':
            if not in_area(y, x+1, area):
                return locations
            if area[y][x+1] != '#':
                position = (y, x+1)
            elif area[y+1][x] != '#':
                position = (y+1, x)
                heading = 'v'
            else:
                heading = '<'
        elif heading == 'v':
            if not in_area(y+1, x, area):
                return locations
            if area[y+1][x] != '#':
                position = (y+1, x)
            elif area[y][x-1] != '#':
                position = (y, x-1)
                heading = '<'
            else:
                heading = '^'
        elif heading == '<':
            if not in_area(y, x-1, area):
                return locations
            if area[y][x-1] != '#':
                position = (y, x-1)
            elif area[y-1][x] != '#':
                position = (y-1, x)
                heading = '^'
            else:
                heading = '>'

for y, row in enumerate(area):
    for x, column in enumerate(row):
        if column != '.' and column != '#':
            position = (y, x)
            heading = column

path = get_path(position, heading, area)

print(len(path))

# Part 2

counter = 0
for y, x in path:
    area[y][x] = '#'
    if not get_path(position, heading, area):
        counter += 1
    area[y][x] = '.'

print(counter)