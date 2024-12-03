# Day 03

with open('./03.txt') as my_input:
    memory = my_input.read()

results = []
mul, x, y = '', '', ''
do_or_dont = 'do()'
more_accurate_results = []
instruction = ''
for char in memory:
    if mul == 'mul(':
        if isinstance(x, int):
            if y and char == ')':
                result = x * int(y)
                results.append(result)
                if do_or_dont == 'do()':
                    more_accurate_results.append(result)
                mul, x, y = '', '', ''
            elif char.isdigit() and len(y) < 3:
                y += char
            else:
                mul, x, y = '', '', ''
        elif x and char == ',':
            x = int(x)
        elif char.isdigit() and len(x) < 3:
            x += char
        else:
            mul, x = '', ''
    elif char == 'mul('[len(mul)]:
        mul += char
    elif char == "don't()"[len(instruction)] or char == 'do()'[len(instruction)]:
        instruction += char
        if instruction in ("don't()", 'do()'):
            do_or_dont = instruction
            instruction = ''

# Part 1

print(sum(results))


# Part 2

print(sum(more_accurate_results))