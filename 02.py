# Day 02

with open('./02.txt') as my_input:
    input_lines = my_input.readlines()

def calculate_differences(report):
    return [next_level - current_level for current_level, next_level in zip(report, report[1:])]

def check_rules(trend, differences):
    return True if trend == 'decreasing' and all(-4 < difference < 0 for difference in differences) or \
                   trend == 'increasing' and all( 0 < difference < 4 for difference in differences) else False

reports = [list(map(int, line.split())) for line in input_lines]

reports_safe = 0
reports_with_a_single_bad_level = 0
for report in reports:
    differences = calculate_differences(report)
    trend = 'increasing' if sum(difference > 0 for difference in differences) > len(differences)/2 else 'decreasing'
    if check_rules(trend, differences):
        reports_safe += 1
        continue
    report_copy = [level for level in report]
    for idx, difference in enumerate(differences):
        if trend == 'decreasing' and not -4 < difference < 0 or trend == 'increasing' and not 0 < difference < 4:
            report.pop(idx)
            report_copy.pop(idx + 1)
            break
    if check_rules(trend, calculate_differences(report)) or check_rules(trend, calculate_differences(report_copy)):
        reports_with_a_single_bad_level += 1

# Part 1

print(reports_safe)

# Part 2

print(reports_safe + reports_with_a_single_bad_level)