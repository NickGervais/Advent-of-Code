### Day 18: Operation Order  ###

equations = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        equations.append(line.rstrip())

import re

VALID_OPERATORS = {'+', '*'}

def find_group(equation_list, i):
    group = []
    par_stack = ['(']
    j = i + 1
    while len(par_stack) != 0:
        if equation_list[j] == ')':
            par_stack.pop()
        j += 1
    group = equation_list[i+1:j-1]
    return group

def equation_list_from_string(equation):
    equation_list = re.findall('(\d+|[^ 0-9])', equation)
    new_equation_list = []
    print(find_group(equation_list, 2))
    for i, val in enumerate(equation_list):
        if val.isdigit():
            new_equation_list.append(int(val))
        elif val in VALID_OPERATORS:
            new_equation_list.append(val)
        elif val == '(':
            group = []
            par_stack = ['(']
            j = i + 1
            while len(par_stack) != 0:
                if equation_list[j] == ')':
                    par_stack.pop()
                    equation_list[i+1:j]
                j += 1
            new_equation_list.append(equation_list[i+1:j-1])




            for j, val1 in enumerate(equation[i+1:])
                if val1 == ')':
                    par_stack



def get_equation_list(equation: str, i: int):
    a = el[i]
    b = el[i+1]
    c = el[i+2]

    if el[i].isdigit() and el[i+1] in VALID_OPERATORS and el[i+2].isdigit():
        return eval(''.join(equation_list))
    elif el[2] == '(':
        return 
    else:




equation_list_from_string(equations[0])

'''
1 -> 2 

val: 1
operation: '+'
child: 2
'''