import os
from aoc_utils import aoc_utils
import numpy as np

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    pos = [int(i) for i in problem_input.split(',')]
    pos = np.array(pos)

    def calc_fuel_cost(cur_pos, destination_pos, level):
        difference = abs(cur_pos - destination_pos)
        if level == 1:
            return difference
        else:
            return difference * (difference + 1) / 2

    if level == 1:
        median = int(np.median(pos))
        fuels = 0
        for p in pos:
            fuels += calc_fuel_cost(p, median, level)
        return fuels

    elif level == 2:
        mean = int(np.mean(pos))
        range_check = int(len(pos) / 8) # arbitrary number to check around mean.
        min_fuels = float('inf')

        for i in range(mean - range_check, mean + range_check + 1):
            fuels = 0
            for p in pos:
                fuels += calc_fuel_cost(p, i, level)
            if fuels < min_fuels:
                min_fuels = fuels
        return int(min_fuels)


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
