import os
from aoc_utils import aoc_utils
from collections import defaultdict
import numpy as np

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    steps = []
    
    x_min = float('inf')
    x_max = float('-inf')
    y_min = float('inf')
    y_max = float('-inf')
    z_min = float('inf')
    z_max = float('-inf')
    
    for line in problem_input.split('\n'):
        switch, cords = line.split(' ')
        x_cords, y_cords, z_cords = cords.split(',')
        x_cords = [int(i) for i in x_cords.replace('x=', '').split('..')]
        y_cords = [int(i) for i in y_cords.replace('y=', '').split('..')]
        z_cords = [int(i) for i in z_cords.replace('z=', '').split('..')]

        if x_cords[0] < x_min:
            x_min = x_cords[1]
        if x_cords[1] > x_max:
            x_max = x_cords[1]

        if y_cords[0] < y_min:
            y_min = y_cords[1]
        if y_cords[1] > y_max:
            y_max = y_cords[1]

        if z_cords[0] < z_min:
            z_min = z_cords[1]
        if z_cords[1] > z_max:
            z_max = z_cords[1]

        steps.append({
            'switch': switch,
            'x': x_cords,
            'y': y_cords,
            'z': z_cords
        })

    print(x_min, x_max)
    print(y_min, y_max)
    print(z_min, z_max)

    if level == 1:
        # init_zone = {
        #     'x': (-50, 50),
        #     'y': (-50, 50),
        #     'z': (-50, 50)
        # }

        # cubes = {}

        # for step in steps:
        #     for x in range(step['x'][0], step['x'][1] +1):
        #         if not init_zone['x'][0] <= x <= init_zone['x'][1]:
        #             continue

        #         for y in range(step['y'][0], step['y'][1] +1):
        #             if not init_zone['y'][0] <= y <= init_zone['y'][1]:
        #                 continue

        #             for z in range(step['z'][0], step['z'][1] +1):
        #                 if not init_zone['z'][0] <= z <= init_zone['z'][1]:
        #                     continue

        #                 if step['switch'] == 'on':
        #                     cubes[(x, y, z)] = True
        #                 else:
        #                     cubes[(x, y, z)] = False
                            

        # total_on = 0
        # for _, on in cubes.items():
        #     if on:
        #         total_on += 1
        
        # return total_on
        return True
    if level == 2:
        total_volume = 0
        prev_offs = []
        prev_ons = []

        for step in reversed(steps):
            if step['switch'] == 'on':
                for off in prev_offs:
                    
                    pass


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
