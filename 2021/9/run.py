import os
from aoc_utils import aoc_utils
import numpy as np
import time

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    l = []
    for line in problem_input.split('\n'):
        l.append(line.strip())
    
    hmap = []
    for i in l:
        hmap.append('.' + i + '.')

    hmap.insert(0, '.'*len(hmap[0]))
    hmap.append('.'*len(hmap[0]))
    for i in hmap:
        print(i)

    adjecent_difs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if level == 1 or level == 2:
        low_points = []
        for y in range(1, len(hmap) - 1):
            for x in range(1, len(hmap[0]) - 1):
                val = hmap[y][x]
                is_low = True
                for y1, x1 in adjecent_difs:
                    comp_val = hmap[y+y1][x+x1]
                    if comp_val != '.' and int(val) >= int(comp_val):
                        is_low = False
                        continue
                if is_low:
                    low_points.append((y, x))

        def calc_basin(y: int, x: int, h_map: list, seen: set = set()):
            val = h_map[y][x]
            # print(y, x, val, seen)
            # time.sleep(0.2)
            if val in ('.', '9'):
                return seen
            
            if f'{y}:{x}' in seen:
                return seen

            seen.add(f'{y}:{x}')
            for y1, x1 in adjecent_difs:
                calc_basin(y+y1, x+x1, h_map, seen)
            
            return seen
            
        basins = []
        for y, x in low_points:
            print('start', y, x)
            seen = set()
            calc_basin(y, x, hmap, seen)
            basins.append(len(seen))
        basins.sort()
        print(basins)

        return np.prod(basins[-3:])


        # result = 0
        # for y, x in low_points:
        #     result += int(hmap[y][x]) +1
        # return result

    if level == 2:
       pass

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
