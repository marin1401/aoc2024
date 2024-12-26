# Day 08

with open('./08.txt') as my_input:
    city = my_input.read().splitlines()

def in_city(y, x, city):
    return y >= 0 and x >= 0 and y < len(city) and x < len(city)

antennas = {}
for y, row in enumerate(city):
    for x, column in enumerate(row):
        if column != '.':
            if not column in antennas.keys():
                antennas[column] = [(y, x)]
            else:
                antennas[column].append((y, x))

# Part 1

antinodes = set()
for antenna, nodes in antennas.items():
    for num, (y1, x1) in enumerate(nodes):
        for (y2, x2) in nodes[num+1:]:
            y0, x0 = y1 - (y2-y1), x1 - (x2-x1)
            if in_city(y0, x0, city):
                antinodes.add((y0, x0))
            y3, x3 = y2 + (y2-y1), x2 + (x2-x1)
            if in_city(y3, x3, city):
                antinodes.add((y3, x3))

print(len(antinodes))

# Part 2

antinodes = set()
for antenna, nodes in antennas.items():
    for num, (y1, x1) in enumerate(nodes):
        for (y2, x2) in nodes[num+1:]:
            y0, x0 = y1, x1
            while in_city(y0, x0, city):
                antinodes.add((y0, x0))
                y0, x0 = y0 - (y2-y1), x0 - (x2-x1)
            y3, x3 = y2, x2
            while in_city(y3, x3, city):
                antinodes.add((y3, x3))
                y3, x3 = y3 + (y2-y1), x3 + (x2-x1)

print(len(antinodes))