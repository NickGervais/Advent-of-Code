from aoc_utils import aoc_utils
import os

year = 2021
day = 2

test_cases = [
    {'level': 1, 'input': '', 'output': 150},
    {'level': 2, 'input': '', 'output': 900}
]

def answer(input, level, test=None):
    instructions = [i.split(' ') for i in input.split('\n')]
    
    if level == 1:
        depth = 0
        horizontal = 0

        for direction, value in instructions:
            if direction == 'forward':
                horizontal += int(value)
            elif direction == 'down':
                depth += int(value)
            elif direction == 'up':
                depth -= int(value)


        return depth * horizontal
    if level == 2:
        aim = 0
        depth = 0
        horizontal = 0

        for direction, value in instructions:
            if direction == 'forward':
                horizontal += int(value)
                depth += aim * int(value)
            elif direction == 'down':
                aim += int(value)
            elif direction == 'up':
                aim -= int(value)

        return depth * horizontal

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
