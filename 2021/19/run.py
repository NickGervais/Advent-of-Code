import os
from aoc_utils import aoc_utils
from collections import defaultdict

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def binary_to_decimal(binary: str) -> int:
    return int(binary, 2)

def answer(problem_input, level, test=None):
    problem_input = problem_input.split('\n')
    ALGO = problem_input.pop(0)
    # remove blank line
    problem_input.pop(0)

    print(ALGO)
    print(problem_input)

    height = len(problem_input)
    width = len(problem_input[0])

    input_image = [[None for _ in range(width)] for _ in range(height)]
    for y, line in enumerate(problem_input):
        for x, c in enumerate(line):
            input_image[y][x] = c
        


    # means all untracked positions will toggle between on and off.
    toggle = ALGO[0] == '#' and ALGO[-1] == '.'
    cur_inf_char = '.'

    if level == 1 or level == 2:
        for _ in range(2):
            new_height = height + 1
            new_width = width + 1
            new_image = [[cur_inf_char for _ in range(new_width)] for _ in range(new_height)]
            for y in range(new_height):
                for x in range(new_width):
                    binary_string = ''
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            y1 = y + i
                            x1 = x + j
                            if 0<= y1 < height and 0<= x1 < width:
                                # in bounds
                                c = input_image[y1][x1]
                            else:
                                # out of bounds
                                c = cur_inf_char

                            binary_string += '1' if c == '#' else '0'
                    
                    decimal = int(binary_string, 2)
                    new_char = ALGO[decimal]
                    new_image[y][x] = new_char
            input_image = new_image
            height += 1
            width += 1
            if toggle:
                cur_inf_char = '#' if cur_inf_char == '.' else '.'
        # print(input_image)

        total_on = 0
        for y in range(height):
            for x in range(width):
                if input_image[y][x] == '#':
                    total_on += 1

        return total_on



        

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
