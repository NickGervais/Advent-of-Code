import os
from aoc_utils import aoc_utils
from collections import defaultdict
import time

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def dfs_backtracking_path_count(cur_cave, cave_map, small_seen, total, level):

    # show that we have visited the small cave
    if cur_cave == cur_cave.lower():
        small_seen[cur_cave] += 1

    # base case: if we reached end then we finished the path.
    if cur_cave == 'end':
        total[0] += 1

    else:
        # loop through adjecent caves
        for next_cave in cave_map[cur_cave]:
            # ignore 'start' cave
            if next_cave != 'start':
                if next_cave == next_cave.upper():  # next is big cave
                    # Visit Big Caves any number of times
                    dfs_backtracking_path_count(next_cave, cave_map, small_seen, total, level)
                else:  # next is small cave or 'end'
                    if small_seen[next_cave] == 0:  # haven't visited small cave yet.
                        dfs_backtracking_path_count(next_cave, cave_map, small_seen, total, level)

                    elif small_seen[next_cave] == 1 and level == 2: # level 2 can visit ONE small cave 2 times.
                        if 2 not in [v for k, v in small_seen.items() if k!=k.upper() and k not in ['start', 'end']]:
                            dfs_backtracking_path_count(next_cave, cave_map, small_seen, total, level)

    # remove small cave from seen.
    # this allows us to visit every possible path permutation.
    if cur_cave == cur_cave.lower():
        small_seen[cur_cave] -= 1


def answer(problem_input, level, test=None):
    cave_map = defaultdict(list)
    for line in problem_input.split('\n'):
        a, b = line.split('-')
        cave_map[a].append(b)
        cave_map[b].append(a)

    print(level)
    if level == 1:
        total = [0]
        seen = defaultdict(int)
        dfs_backtracking_path_count('start', cave_map, seen, total, 1)
        print(total[0])
        return total[0]

    elif level == 2:
        total = [0]
        seen = defaultdict(int)
        dfs_backtracking_path_count('start', cave_map, seen, total, 2)
        print(total[0])
        return total[0]

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
