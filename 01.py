# Day 01

with open('./01.txt') as my_input:
    input_lines = my_input.readlines()

left_list, right_list = zip(*(map(int, line.split()) for line in input_lines))

# Part 1

print(sum(abs(left_number - right_number) for left_number, right_number in zip(sorted(left_list), sorted(right_list))))

# Part 2

print(sum(left_number * right_list.count(left_number) for left_number in left_list))