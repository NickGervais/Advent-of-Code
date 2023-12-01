import os
from aoc_utils import aoc_utils
from collections import deque
import numpy as np
import re

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]


class Cargo:
    def __init__(self, stacks):
        self.stacks = stacks

def print_cargo(cargo):
    for i in cargo:
        print(' '.join(i))


def answer(problem_input, level, test=None):
    cargo_arrangement = []
    moves = []

    input_moves = False
    for line in problem_input.split('\n'):
        if line == "":
            input_moves = True
            continue

        if not input_moves:
            
            print('line length:', len(line))
            row = []
            for i in range(3, len(line) + 1, 4):
                value = line[i-2]
                row.append(value)
            cargo_arrangement.append(row)
        else:
            result = re.search(r"move (\b\d+) from (\b\d+) to (\b\d+)", line.strip())
            moves.append(tuple([int(i) for i in result.groups()]))
        
    cargo_arrangement.pop(-1)

    # rotate list
    cargo_arrangement = np.array(cargo_arrangement)
    cargo_arrangement = np.rot90(cargo_arrangement, 3)
    cargo_arrangement = cargo_arrangement.tolist()
    
    cargo_stacks = []
    cargo_list = []
    for s in cargo_arrangement:
        strip_stack = [i for i in s if i != ' ']
        cargo_stacks.append(deque(strip_stack))
        cargo_list.append(strip_stack)


    print_cargo(cargo_list)

    if level == 1:
        for amount, start, end in moves:
            for _ in range(amount):
                cargo_stacks[end - 1].append(cargo_stacks[start - 1].pop())
            
            # print()
            # print_cargo(cargo_arrangement)
            # print()
        return ''.join([s[-1] for s in cargo_stacks if s[-1] != ' '])
    elif level == 2:
        for amount, start, end in moves:
            print(amount, start, end)
            cargo_list[end - 1].extend(cargo_list[start - 1][-amount:])
            cargo_list[start - 1] = cargo_list[start - 1][:-amount]

            print()
            print_cargo(cargo_list)
        return ''.join([s[-1] for s in cargo_list])

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
