# Day 07

from itertools import product

with open('./07.txt') as my_input:
    equations = my_input.read().splitlines()

results = [equations.split(':')[0] for equations in equations]
numbers = [equations.split(': ')[1].split() for equations in equations]

def get_total_calibration_result(operators, results, numbers):
    total_calibration_result = 0
    for result, values in zip(results, numbers):
        for prod in product(operators, repeat=len(values)-1):
            equation = values[0]
            for operator, value in zip(prod, values[1:]):
                if operator == '||':
                    equation += value
                else:
                    equation = str(eval(equation + operator + value))
            if result == equation:
                total_calibration_result += int(result)
                break
    return total_calibration_result

# Part 1

print(get_total_calibration_result(('+', '*'), results, numbers))


# Part 2

print(get_total_calibration_result(('+', '*', '||'), results, numbers))