### Day 18: Operation Order  ###

equations = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        equations.append(line.rstrip())

# import re

# VALID_OPERATORS = {'+', '*'}

# def find_group(equation_list, i):
#     group = []
#     par_stack = ['(']
#     j = i + 1
#     while len(par_stack) != 0:
#         if equation_list[j] == ')':
#             par_stack.pop()
#         j += 1
#     group = equation_list[i+1:j-1]
#     return group

# def equation_list_from_string(equation):
#     equation_list = re.findall('(\d+|[^ 0-9])', equation)
#     new_equation_list = []
#     print(find_group(equation_list, 2))
#     for i, val in enumerate(equation_list):
#         if val.isdigit():
#             new_equation_list.append(int(val))
#         elif val in VALID_OPERATORS:
#             new_equation_list.append(val)
#         elif val == '(':
#             group = []
#             par_stack = ['(']
#             j = i + 1
#             while len(par_stack) != 0:
#                 if equation_list[j] == ')':
#                     par_stack.pop()
#                     equation_list[i+1:j]
#                 j += 1
#             new_equation_list.append(equation_list[i+1:j-1])




#             for j, val1 in enumerate(equation[i+1:])
#                 if val1 == ')':
#                     par_stack

import numpy

def equation_string_to_list(equation: str):
    import re
    return re.findall('(\d+|[^ 0-9])', equation)

def eval_eq(equation: list):
    result = int(equation[0])
    i = 1
    while i < len(equation):
        # print(result, i)
        if equation[i] == '*':
            result = result * int(equation[i + 1])
            i = i + 2
        elif equation[i] == '+':
            result = result + int(equation[i + 1])
            i = i + 2

    return result

def eval_eq2(equation: list):
    equation = ''.join(equation)
    mult_groups = [eval(i) for i in equation.split('*')]
    return numpy.prod(mult_groups)


def solve_equation(equation: list):
    new_eq = []
    i = 0
    while i < len(equation):
        val = equation[i]
        if val == '(':
            # solve what's in paranthesis
            par_stack = ['(']
            j = i + 1
            while len(par_stack) > 0:
                if equation[j] == '(':
                    par_stack.append('(')
                elif equation[j] == ')':
                    par_stack.pop()
                j += 1
            new_eq.append(solve_equation(equation[i+1:j-1]))
            i = j
        else:
            new_eq.append(val)
            i += 1
    # print(equation, new_eq, eval_eq2(new_eq), '\n')
    return str(eval_eq2(new_eq))

def part_1(equations):
    total_sum = 0
    for equation in equations:
        total_sum += int(solve_equation(equation.replace(' ', '')))

    print(total_sum)

# part_1(equations)
# solution: 31142189909908

def part_2(equations):
    total_sum = 0
    for equation in equations:
        total_sum += int(solve_equation(equation.replace(' ', '')))
    
    print(total_sum)

part_2(equations)
# solution: 323912478287549