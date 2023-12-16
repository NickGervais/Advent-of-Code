import os
from aoc_utils import aoc_utils
import numpy as np

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....''', 'output': 136},
    {'level': 2, 'input': '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....''', 'output': 64},
]


def tilt_column_up(column: tuple) -> list:
    new_column = ['.' for _ in range(len(column))]

    for i, char in enumerate(column):

        if char != "O":
            # only round rocks can move
            new_column[i] = char
            continue

        if i == 0:
            # already at the north border
            new_column[i] = char
            continue

        j = i
        prev_char = new_column[j - 1]
        while j != 0 and prev_char not in ['O', '#']:
            j -= 1
            prev_char = new_column[j - 1]
        new_column[j] = char
    return new_column


def tilt_rock_map_up(rock_map: tuple) -> np.array:
    new_rock_map = []
    for column in rock_map:
        new_column = tilt_column_up(column)
        new_rock_map.append(new_column)

    new_rock_map = np.array(new_rock_map)
    return new_rock_map.T


def get_rock_map_total_load(rock_map):
    total_load = 0
    for i, row in enumerate(reversed(rock_map)):
        total_load += np.count_nonzero(row == 'O') * (i + 1)
    return total_load



def answer(problem_input, level, test=None):
    rock_map = []
    for line in problem_input.split('\n'):
        line = list(line.strip())
        rock_map.append(line)

    rock_map = np.array(rock_map)

    if level == 1:

        new_rock_map = tilt_rock_map_up(tuple(map(tuple, rock_map.T)))
        return get_rock_map_total_load(new_rock_map)

    elif level == 2:
        # 1000000000
        new_rock_map = rock_map
        maps_seen = set()

        # Step 1: find cycle length
        for cycle_num in range(200):
            if cycle_num % 1 == 0:
                print(cycle_num, len(maps_seen))
                # for row in new_rock_map:
                #     print(''.join(row))

            # cycle
            for _ in range(4):
                map_tuple = tuple(map(tuple, new_rock_map.T))
                new_rock_map = tilt_rock_map_up(map_tuple)
                # print(new_rock_map)
                # print()
                new_rock_map = np.rot90(new_rock_map, k=3)

            c_map = tuple(map(tuple, new_rock_map))
            if tuple(map(tuple, c_map)) in maps_seen:
                # first map seen is the cycle!
                break
            maps_seen.add(c_map)

        # Step 2: Jump to the last cycle before 1000000000 and run until 1000000000
        for cycle_num in range(1000000002 - ((1000000000 // cycle_num) * cycle_num)):
            # cycle
            for _ in range(4):
                map_tuple = tuple(map(tuple, new_rock_map.T))
                new_rock_map = tilt_rock_map_up(map_tuple)
                new_rock_map = np.rot90(new_rock_map, k=3)

        return get_rock_map_total_load(new_rock_map)


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
