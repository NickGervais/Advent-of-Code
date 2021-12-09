import os
from aoc_utils import aoc_utils
import numpy as np

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '3,4,3,1,2', 'output': 5934},
    {'level': 2, 'input': '3,4,3,1,2', 'output': 26984457539}
]

def solve (timers, days = 80):
        tracker = [0 for _ in range(9)]
        for i in timers:
            tracker[i] += 1
        tracker = np.array(tracker)

        for _ in range(days):
            # shift array to left. aka mark one day off timers.
            tracker = np.roll(tracker, -1)
            # 0s will become 8s from the shift. 
            # We also want them to become 6s, aka duplicating.
            tracker[6] += tracker[-1]

        return np.sum(tracker)

def answer(problem_input, level, test=None):
    timers = [int(i) for i in problem_input.split(',')]

    if level == 1:
        return solve(timers, 80)
    elif level == 2:
        return solve(timers, 256)
        

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
