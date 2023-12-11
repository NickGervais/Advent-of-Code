import os
from aoc_utils import aoc_utils
from collections import defaultdict
from dataclasses import dataclass
import re
from queue import Queue
from typing import List
import time
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(50000)
print(sys.getrecursionlimit())

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF''', 'output': 4},
    {'level': 1, 'input': '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ''', 'output': 8},
    {'level': 1, 'input': '''F-77-
|FS|7
|||L7
LJL-J
LJ.LJ''', 'output': 5},
]


@dataclass
class Cord:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class PipeMap:
    def __init__(self, raw_input):
        start_cord: Cord = None
        pipe_map = []
        for y, line in enumerate(raw_input.split('\n')):
            new_line = []
            for x, char in enumerate(line.strip()):
                if char == 'S':
                    start_cord = Cord(x=x, y=y)
                new_line.append(char)
            pipe_map.append(new_line)

        self.pipe_map = pipe_map
        self.start_cord = start_cord

    def _cord_in_bounds(self, cord: Cord) -> bool:
        x_len = len(self.pipe_map[0])
        y_len = len(self.pipe_map)
        if cord.x < 0 or (x_len - 1) < cord.x:
            return False

        if cord.y < 0 or (y_len - 1) < cord.y:
            return False

        return True

    def _get_adjacent_cords(self, cord: Cord) -> List[Cord]:
        y = cord.y
        x = cord.x
        adjecent_cords = []
        for y_delta in [-1, 0, 1]:
            for x_delta in [-1, 0, 1]:
                if y_delta == 0 and x_delta == 0:
                    continue

                adj_cord = Cord(x=x + x_delta, y=y + y_delta)
                if not self._cord_in_bounds(adj_cord):
                    continue
                else:
                    adjecent_cords.append(adj_cord)
        return adjecent_cords

    def _adj_cord_matches_char(self, char: str, x_delta: int, y_delta: int) -> bool:
        m = {
            (0, -1): {'|', 'F', '7'},
            (-1, 0): {'-', 'L', 'F'},
            (1, 0): {'-', 'J', '7'},
            (0, 1): {'|', 'J', 'L'}
        }
        if char in m[(x_delta, y_delta)]:
            return True
        else:
            return False

    def _get_adjacent_pipes_backward(self, cord: Cord) -> List[Cord]:
        '''
        No diagonals.
        adjecent pipe must be connected, aka match character based on direction.
        '''
        y = cord.y
        x = cord.x
        adjecent_cords = []
        adj_deltas = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        for x_delta, y_delta in adj_deltas:
            if y_delta == 0 and x_delta == 0:
                continue

            adj_cord = Cord(x=x + x_delta, y=y + y_delta)
            if not self._cord_in_bounds(adj_cord):
                continue

            adj_char = self.pipe_map[adj_cord.y][adj_cord.x]
            if not self._adj_cord_matches_char(adj_char, x_delta, y_delta):
                continue

            adjecent_cords.append(adj_cord)
        return adjecent_cords

    def _get_adjacent_pipes(self, cord: Cord) -> List[Cord]:
        '''
        No diagonals.
        adjecent pipe must be connected, aka match character based on direction.
        '''
        y = cord.y
        x = cord.x
        # adj_deltas = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        north = (0, -1)
        south = (0, 1)
        east = (1, 0)
        west = (-1, 0)
        adj_deltas_by_char = {
            '-': [east, west],
            '|': [north, south],
            'L': [north, east],
            'J': [north, west],
            '7': [south, west],
            'F': [south, east],
            '.': []
        }

        current_char = self.pipe_map[y][x]
        if current_char == 'S':
            return self._get_adjacent_pipes_backward(cord)

        adj_deltas = adj_deltas_by_char[current_char]

        adjecent_cords = []
        for x_delta, y_delta in adj_deltas:
            if y_delta == 0 and x_delta == 0:
                continue

            adj_cord = Cord(x=x + x_delta, y=y + y_delta)
            if not self._cord_in_bounds(adj_cord):
                continue

            adjecent_cords.append(adj_cord)
        return adjecent_cords

    def _print_map(self, m):
        for line in m:
            print(line)

    def _dfs(self, cord: Cord, visited: set, depth: int, distance_tracker):
        # time.sleep(0.5)

        visited.add(cord)
        distance_tracker[cord.y][cord.x] = depth
        # self._print_map(distance_tracker)
        # print()

        adj_pipe_cords = self._get_adjacent_pipes(cord)
        for adj_cord in adj_pipe_cords:
            if adj_cord not in visited:
                self._dfs(adj_cord, visited, depth+1, distance_tracker)

    def dfs(self):
        visited = set()
        distance_tracker = [['x' for _ in range(len(self.pipe_map[0]))] for _ in range(len(self.pipe_map))]
        print(self.start_cord)
        self._dfs(self.start_cord, visited, 0, distance_tracker)

        distances = []
        for line in distance_tracker:
            for i in line:
                if i is not 'x':
                    distances.append(i)
        return int((max(distances) + 1) / 2)

    def part_1(self):
        distance_tracker = [[None for _ in range(len(self.pipe_map[0]))] for _ in range(len(self.pipe_map))]

        q = Queue()
        q.put((self.start_cord, 0))

        while not q.empty():
            cur_cord, cord_dist = q.get()
            print(cur_cord)
            self._print_map(distance_tracker)
            print()
            if distance_tracker[cur_cord.y][cur_cord.x] != None:
                return distance_tracker[cur_cord.y][cur_cord.x]

            else:
                distance_tracker[cur_cord.y][cur_cord.x] = cord_dist
                adj_pipe_cords = self._get_adjacent_pipes(cur_cord)
                for c in adj_pipe_cords:
                    q.put((c, cord_dist + 1))

        # distances = []
        # for line in distance_tracker:
        #     for i in line:
        #         if i is not None:
        #             distances.append(i)

        self._print_map(distance_tracker)
        # return max(distances)


def answer(problem_input, level, test=None):
    pipe_map = PipeMap(problem_input)

    if level == 1:
        return pipe_map.dfs()

    elif level == 2:
        return 0


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
