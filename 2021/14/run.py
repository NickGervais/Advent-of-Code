import os
from aoc_utils import aoc_utils
from collections import defaultdict

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    lines = []
    for line in problem_input.split('\n'):
        lines.append(line.strip())

    if level == 1 or level == 2:
        for l in lines:
            pass
        return

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
