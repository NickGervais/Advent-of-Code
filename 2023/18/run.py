import os
from aoc_utils import aoc_utils
from collections import defaultdict
from dataclasses import dataclass
import re
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.ops import unary_union
import numpy as np


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)''', 'output': 62},
    {'level': 2, 'input': '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)''', 'output': 952408144115},
]


@dataclass
class Cord:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __lt__(self, other):
        return True


right = Point(1, 0)
down = Point(0, 1)
left = Point(-1, 0)
up = Point(0, -1)

direction_map = {
    'R': right,
    'D': down,
    'L': left,
    'U': up
}

int_to_dir_char = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U'
}


def get_next_point(cur_point: Point, dir_char: str, length: int):
    delta_point = direction_map[dir_char]

    x_delta = delta_point.x * int(length)
    y_delta = delta_point.y * int(length)

    return Point(cur_point.x + x_delta, cur_point.y + y_delta)


def answer(problem_input, level, test=None):
    points = []
    points_part_2 = []

    cur_point = Point(0, 0)
    cur_point_part_2 = Point(0, 0)
    for line in problem_input.split('\n'):
        points.append(cur_point)
        points_part_2.append(cur_point_part_2)

        dir_char, length, hex_code = line.strip().split(' ')

        cur_point = get_next_point(cur_point, dir_char, length)

        part_2_dir_char = int_to_dir_char[int(hex_code[-2])]
        part_2_length = int(hex_code[2:-2], 16)

        cur_point_part_2 = get_next_point(cur_point_part_2, part_2_dir_char, part_2_length)


    if level == 1:
        polygon = Polygon(points)
        min_x, min_y, max_x, max_y = polygon.bounds

        X, Y = np.meshgrid(np.arange(min_x, max_x, 1), np.arange(min_y, max_y, 1))

        #create a iterable with the (x,y) coordinates
        points = zip(X.flatten(), Y.flatten())

        print(len([i for i in points if Point(i[0], i[1]).touches(polygon) or Point(i[0], i[1]).within(polygon)]))
        print(polygon.length)
        print(polygon.area)

        total_points = 0
        for y in range(int(min_y), int(max_y) + 1):
            row = ''
            for x in range(int(min_x), int(max_x) + 1):
                p = Point(x, y)
                if p.touches(polygon):
                    total_points += 1
                    row += 'E'
                elif p.within(polygon):
                    total_points += 1
                    row += '#'
                else:
                    row += '.'
            print(row)
        return total_points

    elif level == 2:
        polygon = Polygon(points_part_2)
        min_x, min_y, max_x, max_y = polygon.bounds
        print(polygon.area)
        # total_points = 0
        # for y in range(int(min_y), int(max_y) + 1):
        #     row = ''
        #     for x in range(int(min_x), int(max_x) + 1):
        #         p = Point(x, y)
        #         if p.touches(polygon) or p.within(polygon):
        #             total_points += 1
        #             row += '#'
        #         else:
        #             row += '.'
        #     # print(row)
        # return total_points

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
