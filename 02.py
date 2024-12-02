# Day 02

with open('./02.txt') as my_input:
    input_lines = my_input.readlines()

def calculate_differences(report):
    return [next_level - current_level for current_level, next_level in zip(report, report[1:])]

def check_rules(trend, differences):
    return trend == 'decreasing' and all(-4 < difference < 0 for difference in differences) or \
           trend == 'increasing' and all( 0 < difference < 4 for difference in differences)

def bad_level_check(trend, difference):
    return trend == 'decreasing' and not -4 < difference < 0 or trend == 'increasing' and not 0 < difference < 4

reports = [list(map(int, line.split())) for line in input_lines]

reports_safe = 0
reports_with_a_single_bad_level = 0
for report in reports:
    differences = calculate_differences(report)
    trend = 'increasing' if sum(difference > 0 for difference in differences) > len(differences)/2 else 'decreasing'
    if check_rules(trend, differences):
        reports_safe += 1
        continue
    bad_level_index = next(idx for idx, difference in enumerate(differences) if bad_level_check(trend, difference))
    if  check_rules(trend, calculate_differences(report[:bad_level_index]     + report[bad_level_index + 1:])) or \
        check_rules(trend, calculate_differences(report[:bad_level_index + 1] + report[bad_level_index + 2:])):
            reports_with_a_single_bad_level += 1

# Part 1

print(reports_safe)

# Part 2

print(reports_safe + reports_with_a_single_bad_level)
