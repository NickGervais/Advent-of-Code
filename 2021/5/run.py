import os
from aoc_utils import aoc_utils

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def calc_points_in_line(x1, y1, x2, y2, level=1):
    cords = []

    if x1 == x2:
        # vertical
        for i in range(min(y1, y2), max(y1, y2)+1):
            cords.append((x1, i))

    elif y1 == y2:
        # horizontal
        for i in range(min(x1, x2), max(x1, x2)+1):
            cords.append((i, y1))
    
    elif level == 2:
        # diagonal (only in level 2)
        if x1 < x2:
            a = x1, y1
            b = x2, y2
        else:
            a = x2, y2
            b = x1, y1

        x_cords = list(range(a[0], b[0]+1))
        y_cords = list(range(min(y1, y2), max(y1, y2)+1))

        if b[1] < a[1]:
            y_cords.reverse()

        for x, y in zip(x_cords, y_cords):
            cords.append((x, y))

    return cords

def answer(problem_input, level, test=None):
    lines = []
    for line in problem_input.split('\n'):
        a, b = line.split(' -> ')
        x1, y1 = [int(i) for i in a.split(',')]
        x2, y2 = [int(i) for i in b.split(',')]
        lines.append([(x1, y1), (x2, y2)])

    cords_map = {} # (x, y): count

    if level == 1 or level ==2:
        for a, b in lines:
            x1, y1 = a
            x2, y2 = b
            cur_cords = calc_points_in_line(x1, y1, x2, y2, level=level)
            for x, y in cur_cords:
                if (x, y) in cords_map:
                    cords_map[(x,y)] += 1
                else:
                    cords_map[(x,y)] = 1

        result = 0
        for cords, val in cords_map.items():
            if val >= 2:
                result += 1

        return result

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
