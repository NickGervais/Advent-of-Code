import os
from aoc_utils import aoc_utils
import numpy as np
from typing import List, Dict
import math


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#''', 'output': 405},
    {'level': 1, 'input': '''....###...#..##
#..####..##..##
.###..###.#.###
...####...#####
#..#..#..##..##
#.##..##.#.....
#........#.##..''', 'output': 14},
    {'level': 1, 'input': '''#....#.#.
####.##.#
#.##..###
##..#.###
.#....#.#
...##..##
##..#....
##..#....
...##..##
.#....#.#
##..#.###
#.##..###
####.##.#
#....#.#.
.#...#...
.#...#...
#....#.##''', 'output': 700},
]


def confirm_mirror_index(plot, mirror_index) -> bool:
    num_columns = plot.shape[1]
    delta = 0
    while True:
        minor_index = math.floor(mirror_index - delta)
        major_index = math.ceil(mirror_index + delta)

        if minor_index < 0 or major_index >= num_columns:
            return True

        minor_column = plot[:, minor_index]
        major_column = plot[:, major_index]

        if ''.join(minor_column) != ''.join(major_column):
            return False

        delta += 1

def find_mirror_index(plot):
    column_index_map: Dict[str, int] = {}

    mirror_index = -1
    num_columns = plot.shape[1]
    for col_index in range(num_columns):
        column = plot[:, col_index]
        col_hash = ''.join(column)

        if col_hash in column_index_map:
            found_col_index = column_index_map[col_hash]

            mirror_index = abs(found_col_index - col_index) / 2 + float(min(found_col_index, col_index))
            if confirm_mirror_index(plot, mirror_index):
                return math.ceil(mirror_index)

        column_index_map[col_hash] = col_index

    return 0


def find_mirror_index_2(plot, tolerance=0):

    num_rows = plot.shape[0]
    for row_i in range(1, num_rows):
        mirror_depth = min(abs(row_i - 0), abs(row_i - num_rows))

        left_reflection = plot[row_i - mirror_depth:row_i]
        right_reflection = plot[row_i:row_i + mirror_depth]

        differences = left_reflection - np.flip(right_reflection, axis=0)

        if np.sum(np.abs(differences) == 1) == tolerance:
            return row_i
    return 0


def answer(problem_input, level, test=None):
    plots: List[np.array] = []
    for plot in problem_input.split('\n\n'):

        new_plot = []
        for line in plot.split('\n'):
            line = line.strip()
            new_plot.append([1 if i == '#' else 0 for i in line])

        plots.append(np.array(new_plot))

    if level == 1:
        num_cols = 0
        num_rows = 0
        for plot in plots:

            row_mirror_index = find_mirror_index_2(plot)
            num_rows += row_mirror_index

            col_mirror_index = find_mirror_index_2(plot.T)
            num_cols += col_mirror_index

        return num_cols + (100 * num_rows)

    elif level == 2:
        num_cols = 0
        num_rows = 0
        for plot in plots:

            row_mirror_index = find_mirror_index_2(plot, tolerance=1)
            num_rows += row_mirror_index

            col_mirror_index = find_mirror_index_2(plot.T, tolerance=1)
            num_cols += col_mirror_index

        return num_cols + (100 * num_rows)


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
