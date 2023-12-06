import os
from aoc_utils import aoc_utils


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]


def answer(problem_input, level, test=None):
    lines = []
    for line in problem_input.split('\n'):
        line = line.strip()
        lines.append(line)

    if level == 1:
        return 0

    elif level == 2:
        return 0


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
