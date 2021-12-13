import os
import time
from aoc_utils import aoc_utils
from collections import defaultdict

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def print_paper(cords):
    max_x = -1
    max_y = -1
    for x, y in cords:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    
    board = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in cords:
        board[y][x] = '#'
    
    for line in board:
        print(''.join(line))

def answer(problem_input, level, test=None):
    instructions = []
    cords = set()
    for line in problem_input.split('\n'):
        if not line:
            continue
        elif line.startswith('fold along'):
            cord, val = line.replace('fold along ', '').strip().split('=')
            instructions.append([cord, int(val)])
        else:
            x, y = line.strip().split(',')
            cords.add((int(x), int(y)))

    if level == 1 or level == 2:
        level_1_result = None
        for i, inst in enumerate(instructions):
            cord, val = inst

            if i == 1 and level == 1:
                level_1_result = len(cords)
                break

            new_cords = set()
            for x, y in cords:
                new_y = y
                new_x = x
                if cord == 'y':
                    if y > val:
                        new_y = y - ((y - val) * 2)
                elif cord == 'x':
                    if x > val:
                        new_x = x - ((x - val) * 2)
                new_cords.add((new_x, new_y))
            cords = new_cords

        if level == 2:
            print_paper(cords)
            
        return level_1_result

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
