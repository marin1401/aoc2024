# Day 05

with open('./05.txt') as my_input:
    rules, updates = my_input.read().split('\n\n')

rules = [tuple(map(int, rule.split('|'))) for rule in rules.splitlines()]
updates = [tuple(map(int, update.split(','))) for update in updates.splitlines()]

correctly_ordered_middle_page_numbers_sum = 0
incorrectly_ordered_middle_page_numbers_sum = 0

for pages in updates:
    order = True
    for before, after in rules:
        if before in pages and after in pages:
            if pages.index(before) > pages.index(after):
                order = False
    if order:
        correctly_ordered_middle_page_numbers_sum += pages[len(pages)//2]
    else:
        pages_rules = [(before, after) for before, after in rules if before in pages and after in pages]
        befores, afters = map(list, zip(*pages_rules))
        ordered = []
        while len(ordered) < len(pages)-1:
            for idx, (before, after) in enumerate(pages_rules):
                if before not in afters:
                    if before not in ordered:
                        ordered.append(before)
                    afters[idx] = None
        incorrectly_ordered_middle_page_numbers_sum += ordered[len(ordered)//2]

# Part 1

print(correctly_ordered_middle_page_numbers_sum)

# Part 2

print(incorrectly_ordered_middle_page_numbers_sum)