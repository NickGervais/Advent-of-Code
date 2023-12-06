import os
from aoc_utils import aoc_utils
import math


year, day = os.getcwd().split('/')[-2:]

test_cases = [
#     {'level': 1, 'input': '''Time:      7  15   30
# Distance:  9  40  200''', 'output': 288},
]


def answer(problem_input, level, test=None):
    # time, distance = problem_input.split('\n')
    # times = [7, 15, 30]
    # distances = [9, 40, 200]

    if level == 1:
        times = [40, 81, 77, 72]
        distances = [219, 1012, 1365, 1089]
        amount_beat = [0, 0, 0, 0]
        for x, time_alotment in enumerate(times):
            for i in range(0, time_alotment + 1):
                velocity = i
                remaineder_time = time_alotment - i

                distance = remaineder_time * velocity
                if distance > distances[x]:
                    amount_beat[x] += 1
        return math.prod(amount_beat)

    elif level == 2:
        # time_alotment = 71530
        # max_distance = 940200
        time_alotment = 40817772
        max_distance = 219101213651089
        amount_beat = 0
        for i in range(0, time_alotment + 1):
            velocity = i
            remaineder_time = time_alotment - i

            distance = remaineder_time * velocity
            if distance > max_distance:
                amount_beat += 1
        return amount_beat


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
