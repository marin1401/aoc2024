# Day 10

with open('./10.txt') as my_input:
    hiking_map = my_input.read().splitlines()

hiking_map = [tuple(map(int, row)) for row in hiking_map]

def in_area(y, x, area):
    return y >= 0 and x >= 0 and y < len(area) and x < len(area)

def go(height, y, x):
    for yn, xn in [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]:
        if in_area(yn, xn, hiking_map):
            if height + 1 == hiking_map[yn][xn]:
                if height + 1 == 9:
                    ends.add((yn, xn))
                    rating[0] += 1
                else:
                    go(height + 1, yn, xn)

starts = []
for y, row in enumerate(hiking_map):
    for x, column in enumerate(row):
        if not column:
            starts.append((y, x))

score = 0
rating = [0]
for y, x in starts:
    ends = set()
    go(0, y, x)
    score += len(ends)

# Part 1

print(score)

# Part 2

print(rating[0])