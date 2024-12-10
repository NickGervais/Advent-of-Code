import os
from aoc_utils import aoc_utils
from collections import defaultdict
from dataclasses import dataclass
import re
from typing import List, Dict, Optional, Set, Tuple
import math
import time
import sys
from queue import PriorityQueue
import heapq

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533''', 'output': 102},
    {'level': 2, 'input': '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533''', 'output': 94},
    {'level': 2, 'input': '''111111111111
999999999991
999999999991
999999999991
999999999991''', 'output': 71},
]


@dataclass
class Cord:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        # Compare the coordinates based on some criterion (e.g., x value)
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y


@dataclass
class Cell:
    f: int
    h: int
    g: int
    heat_loss: int
    parent: Optional[Cord] = None


right = Cord(x=1, y=0)
down = Cord(x=0, y=1)
left = Cord(x=-1, y=0)
up = Cord(x=0, y=-1)

opposite_delta = {
    right: left,
    down: up,
    left: right,
    up: down
}

dir_to_char = {
    right: '>',
    down: 'v',
    left: '<',
    up: '^'
}

class GearFactoryMap:
    def __init__(self, problem_input: str):
        city_map = []
        for line in problem_input.split('\n'):
            row = list(map(int, line.strip()))
            city_map.append(row)

        self.city_map = city_map

    def part_1(self):
        destination = Cord(x=len(self.city_map)-1, y=len(self.city_map[0])-1)
        return self.astar(Cord(x=0, y=0), destination, 0, 3)

    def part_2(self):
        destination = Cord(x=len(self.city_map)-1, y=len(self.city_map[0])-1)
        return self.astar(Cord(x=0, y=0), destination, 4, 10)

    def heuristic(self, cord: Cord):
        return 0

    def astar(self, start: Cord, goal: Cord, min: int, max):
        @dataclass
        class State:
            cord: Cord
            direction: Cord
            direction_length: int

            def __hash__(self) -> int:
                return hash((self.cord, self.direction, self.direction_length))

            def __lt__(self, other):
                return True

        open_set: PriorityQueue = PriorityQueue()
        cost_so_far: Dict[State, int] = {}
        cord_parent: Dict[State, State] = {}

        start_state = State(cord=start, direction=None, direction_length=0)
        open_set.put((0, start_state))
        cost_so_far[start_state] = 0
        cord_parent[State(cord=start, direction=None, direction_length=0)] = State(cord=None, direction=None, direction_length=None)

        answer = 0
        while not open_set.empty():
            # time.sleep(0.5)
            _, cur_state = open_set.get()

            if cur_state.cord == goal:
                print("GOAL", cost_so_far[cur_state])
                answer = cost_so_far[cur_state]
                break

            for delta in self._get_adjacent_deltas(cur_state.direction, cur_state.direction_length, min, max):

                next_cord = Cord(x=cur_state.cord.x + delta.x, y=cur_state.cord.y + delta.y)
                if not self._cord_in_bounds(next_cord):
                    continue

                next_direction_length = cur_state.direction_length + 1 if delta == cur_state.direction else 1
                next_state = State(cord=next_cord, direction=delta, direction_length=next_direction_length)
                new_cost = cost_so_far[cur_state] + self.city_map[next_cord.y][next_cord.x]

                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost

                    open_set.put((new_cost, next_state))
                    cord_parent[next_state] = cur_state

        path = []
        current = cur_state
        while current.cord != start:
            path.append(current.cord)
            current = cord_parent[current]
        print(path)

        path_set = set(path)
        for y, row in enumerate(self.city_map):
            line = []
            for x, char in enumerate(row):
                if Cord(x=x, y=y) in path_set:
                    line.append('#')
                else:
                    line.append(str(char))
            print(''.join(line))

        return answer

    def _cord_in_bounds(self, cord: Cord) -> bool:
        x_len = len(self.city_map[0])
        y_len = len(self.city_map)
        if cord.x < 0 or (x_len - 1) < cord.x:
            return False

        if cord.y < 0 or (y_len - 1) < cord.y:
            return False

        return True

    def _get_adjacent_deltas(self, direction: Cord, direction_count: int, min_direction_length: int, max_direction_length: int) -> List[Cord]:
        # adj_deltas = [right, down, left, up]

        # if direction is None:
        #     return adj_deltas

        # adj_deltas.remove(opposite_delta[direction])  # cannot go backwards

        # if direction_count < min_direction_length:
        #     return [direction]  # has to go straight for min distance

        # if direction_count == max_direction_length:
        #     adj_deltas.remove(direction)  # can't go straight anymore

        # return adj_deltas
        for delta in [right, down, left, up]:
            if direction is not None:
                if delta == opposite_delta[direction]:
                    continue
                if delta == direction and direction_count == max_direction_length:
                    continue
                if delta not in (opposite_delta[direction], direction) and direction_count < min_direction_length:
                    continue
            yield delta


def answer(problem_input, level, test=None):
    gear_map = GearFactoryMap(problem_input)

    if level == 1:
        return gear_map.part_1()

    elif level == 2:
        return gear_map.part_2()


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
