import os
from aoc_utils import aoc_utils
from collections import defaultdict
from dataclasses import dataclass
import re
from queue import Queue
import copy
import time

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....''', 'output': 46},
    {'level': 2, 'input': r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....''', 'output': 51},
]


right = (1, 0)
down = (0, 1)
left = (-1, 0)
up = (0, -1)

directions = {
    '\\': {
        right: [down],
        down: [right],
        left: [up],
        up: [left]
    },
    '/': {
        right: [up],
        up: [right],
        left: [down],
        down: [left]
    },
    '|': {
        right: [up, down],
        left: [up, down],
        up: [up],
        down: [down]
    },
    '-': {
        right: [right],
        left: [left],
        up: [left, right],
        down: [left, right]
    },
    '.': {
        right: [right],
        left: [left],
        up: [up],
        down: [down]
    },
}

dir_to_char = {
    right: '>',
    left: '<',
    down: 'v',
    up: '^'
}


def cord_in_bounds(mirror_map, cord):
    x_len = len(mirror_map[0])
    y_len = len(mirror_map)
    if cord[0] < 0 or (x_len - 1) < cord[0]:
        return False

    if cord[1] < 0 or (y_len - 1) < cord[1]:
        return False

    return True


def get_number_of_visited_cords(mirror_map, start_cord, start_delta, debug=False):
    heat_map_cord_set = set()
    heat_map_set = set()
    heat_map = copy.deepcopy(mirror_map)

    q = Queue()
    q.put((start_cord, start_delta))

    while not q.empty():
        if debug:
            time.sleep(0.5)
            for line in heat_map:
                print(''.join(line))
            print()

        cur_cord, cur_delta = q.get()

        if (cur_cord, cur_delta) in heat_map_set:
            continue
        heat_map_set.add((cur_cord, cur_delta))
        heat_map_cord_set.add(cur_cord)

        if debug:
            if heat_map[cur_cord[1]][cur_cord[0]] == '.':
                heat_map[cur_cord[1]][cur_cord[0]] = dir_to_char[cur_delta]

        cur_char = mirror_map[cur_cord[1]][cur_cord[0]]
        for next_delta in directions[cur_char][cur_delta]:
            next_x = cur_cord[0] + next_delta[0]
            next_y = cur_cord[1] + next_delta[1]
            next_cord = (next_x, next_y)

            if cord_in_bounds(mirror_map, next_cord):
                q.put((next_cord, next_delta))

    if debug:
        for line in heat_map:
            print(''.join(line))

    return len(heat_map_cord_set)


def answer(problem_input, level, test=None):
    mirror_map = []
    for line in problem_input.split('\n'):
        line = line.strip()
        mirror_map.append(list(line))

    if level == 1:
        return get_number_of_visited_cords(mirror_map, (0, 0), right)

    elif level == 2:

        num_rows = len(mirror_map)
        num_cols = len(mirror_map[0])

        left_cords = []
        right_cords = []
        for i in range(num_rows):
            left_cords.append(((0, i), right))
            right_cords.append(((num_cols - 1, i), left))

        top_cords = []
        bottom_cords = []
        for i in range(num_cols):
            top_cords.append(((i, 0), down))
            bottom_cords.append(((i, num_rows - 1), up))

        max_enerigized = -1
        for start_cord, start_delta in left_cords + right_cords + top_cords + bottom_cords:
            energized = get_number_of_visited_cords(mirror_map, start_cord, start_delta)
            if energized > max_enerigized:
                max_enerigized = energized

        return max_enerigized


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
