import os
from aoc_utils import aoc_utils
from collections import defaultdict
from dataclasses import dataclass
import re

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....''', 'output': 374},
#     {'level': 2, 'input': '''...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....''', 'output': 1030},
]


@dataclass
class Cord:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Universe:
    def _print_map(self, m):
        for i in m:
            print(i)

    def __init__(self, problem_input: str):
        universe_map = []
        empty_row_indexes = []
        empty_column_indexes = []

        for y, line in enumerate(problem_input.split('\n')):
            if all(i == '.' for i in line):
                empty_row_indexes.append(y)

            universe_map.append(list(line))

        self._print_map(universe_map)

        num_rows = len(universe_map)
        num_cols = len(universe_map[0])
        for x in range(num_cols):
            col_values = [universe_map[y][x] for y in range(num_rows)]
            if all(i == '.' for i in col_values):
                empty_column_indexes.append(x)

        print(f'{empty_row_indexes=}, {empty_column_indexes=}')
        self.empty_row_indexes = empty_row_indexes
        self.empty_column_indexes = empty_column_indexes

        # find galaxy
        galaxy_cords = []
        for y, row in enumerate(universe_map):
            for x, char in enumerate(row):
                if char == '#':
                    galaxy_cords.append(Cord(x=x, y=y))

        self.universe_map = universe_map
        self.galaxy_cords = galaxy_cords

    # def brute_force(self):
    #     # expand universe
    #     for y, row in enumerate(self.universe_map):
    #         for idx in reversed(sorted(self.empty_column_indexes)):
    #             row.insert(idx, '.')

    #     for idx in reversed(sorted(self.empty_row_indexes)):
    #         self.universe_map.insert(idx, ['.' for _ in range(len(self.universe_map[0]))])

    #     # find galaxy
    #     galaxy_cords = []
    #     for y, row in enumerate(self.universe_map):
    #         for x, char in enumerate(row):
    #             if char == '#':
    #                 galaxy_cords.append(Cord(x=x, y=y))

    #     sum_of_min = 0
    #     for a, a_cord in enumerate(galaxy_cords):
    #         for b_cord in galaxy_cords[a + 1:]:
    #             if a_cord == b_cord:
    #                 continue

    #             distance = abs(b_cord.y - a_cord.y) + abs(b_cord.x - a_cord.x)
    #             sum_of_min += distance
    #     return sum_of_min

    def sum_of_min_paths(self, expand_size: int) -> int:
        sum_of_min = 0
        for a, a_cord in enumerate(self.galaxy_cords):
            for b_cord in self.galaxy_cords[a + 1:]:
                if a_cord == b_cord:
                    continue

                max_y = max(b_cord.y, a_cord.y)
                min_y = min(b_cord.y, a_cord.y)
                max_x = max(b_cord.x, a_cord.x)
                min_x = min(b_cord.x, a_cord.x)

                crossed_empty_rows = sum([1 for y in self.empty_row_indexes if y in range(min_y, max_y)])
                crossed_empty_cols = sum([1 for x in self.empty_column_indexes if x in range(min_x, max_x)])

                distance = (max_y - min_y) + (crossed_empty_rows * expand_size) + (max_x - min_x) + (crossed_empty_cols * expand_size)
                sum_of_min += distance
        return sum_of_min


def answer(problem_input, level, test=None):
    universe = Universe(problem_input)

    if level == 1:
        return universe.sum_of_min_paths(1)

    elif level == 2:
        return universe.sum_of_min_paths(1000000 - 1)


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
