import os
from aoc_utils import aoc_utils

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    l = []
    il = []
    for line in problem_input.split('\n'):
        l.append(line.strip())
        il.append(int(line.strip()))

    if level == 1:
        a = 0
        for i in il:
            a += i
        return

    if level == 2:
        a = 0
        for i in il:
            a += i
        return

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
