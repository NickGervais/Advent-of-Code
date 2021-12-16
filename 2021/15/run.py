import os
from aoc_utils import aoc_utils
from collections import defaultdict
from queue import PriorityQueue
import time
import math

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

adj_cords = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs_backtracking_path_count(y, x, cave_map, seen, danger_val, min_danger):
    '''
    BAD SOLUTION.
    This looks at every possible path permutation.

    (N + N)! / (N! * N!).
    So if N == 10, Then there are 184,756 permutations.

    If N == 100 (the len of the input)
    There are (9.05 * 10^58) That is a very large number...
    '''
    # show that we have visited the position
    seen[(y, x)] += 1
    danger_val += cave_map[y][x]


    # base case: if we reached the destination then we finished the path.
    if (y, x) == (len(cave_map) -1, len(cave_map[0]) -1):
        if danger_val < min_danger[0]:
            min_danger[0] = danger_val

    else:
        # loop through adjecent caves
        for y_diff, x_diff in adj_cords:
            next_y, next_x = y + y_diff, x + x_diff
            # next cords are in bounds, and not already seen.
            if 0<=next_y< len(cave_map) and 0<=next_x< len(cave_map[0]) and seen[(next_y, next_x)] == 0:
                dfs_backtracking_path_count(next_y, next_x, cave_map, seen, danger_val, min_danger)


    # remove position from seen
    # this allows us to visit every possible path permutation.
    seen[(y, x)] -= 1
    danger_val -= cave_map[y][x]


def astar(start, end, grid):
    path_weights = {}
    previous = {}
    remaining = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            weight = float('inf')
            if (y, x) == start:
                weight = 0

            path_weights[(y, x)] = weight
            remaining.add((y, x))
            previous[(y, x)] = None
    
    while len(remaining) > 0:
        a = {cords: val for cords, val in path_weights.items() if cords in remaining}
        n = min(a, key=a.get)
        weight = path_weights[n]
        y, x = n

        for y_dif, x_dif in adj_cords:
            y_next, x_next = y + y_dif, x + x_dif
            if 0 <= y_next < len(grid) and 0 <= x_next < len(grid[0]):
                
                heuristic = math.sqrt((y_next - end[0])**2 + (x_next - end[1])**2)
                new_path_weight = weight + grid[y_next][x_next] + heuristic
                if new_path_weight < path_weights[(y_next, x_next)]:
                    path_weights[(y_next, x_next)] = new_path_weight
                    previous[(y_next, x_next)] = n
        
        remaining.remove(n)

    cur_cords = end
    total = 0
    while cur_cords != start:
        val = grid[cur_cords[0]][cur_cords[1]]
        total += val
        print(total, val, cur_cords)
        cur_cords = previous[cur_cords]

    return total


def dijkstra(start, end, grid):
    path_weights = {}
    previous = {}
    remaining = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            weight = float('inf')
            if (y, x) == start:
                weight = 0

            path_weights[(y, x)] = weight
            remaining.add((y, x))
            previous[(y, x)] = None
    
    while len(remaining) > 0:
        print(f'remaining: {len(remaining)}/{len(grid)**2}')
        a = {cords: val for cords, val in path_weights.items() if cords in remaining}
        n = min(a, key=a.get)
        weight = path_weights[n]
        y, x = n

        for y_dif, x_dif in adj_cords:
            y_next, x_next = y + y_dif, x + x_dif
            if 0 <= y_next < len(grid) and 0 <= x_next < len(grid[0]):
                
                new_path_weight = weight + grid[y_next][x_next]
                if new_path_weight < path_weights[(y_next, x_next)]:
                    path_weights[(y_next, x_next)] = new_path_weight
                    previous[(y_next, x_next)] = n
        
        remaining.remove(n)

    path = set()
    cur_cords = end
    while cur_cords != start:
        path.add(cur_cords)
        pre_cords = previous[cur_cords]
        # print(pre_cords)
        cur_cords = pre_cords

    # for y in range(len(grid)):
    #     line = ''
    #     for x in range(len(grid[0])):
    #         if (y, x) in path:
    #             line += str(grid[y][x])
    #         else:
    #             line += ' '
    #     print(line)

    return path_weights[end]

def bfs_priority(start, end, grid):
    q = PriorityQueue()
    q.put((0, start))
    seen = set([start])

    while not q.empty():
        print(f'remaining: {q.qsize()}/{len(grid)*2}')
        danger, cords = q.get()
        y, x = cords

        for yd, xd in adj_cords:
            yn, xn = y+yd, x+xd
            if 0 <= yn < len(grid) and 0 <= xn < len(grid[0]):
                if (yn, xn) == end:
                    return danger + grid[yn][xn]
                elif (yn, xn) not in seen:
                    cur_danger = danger + grid[yn][xn]
                    q.put((cur_danger, (yn, xn)))
                    seen.add((yn, xn))

def answer(problem_input, level, test=None):
    danger_map = []
    for line in problem_input.split('\n'):
        danger_map.append([int(i) for i in line.strip()])

    if level == 1:
        return bfs_priority((0, 0), (len(danger_map) -1, len(danger_map[0]) - 1), danger_map)
    elif level == 2:
        new_danger_map = [[0 for _ in range(len(danger_map[0]) * 5)] for _ in range(len(danger_map) * 5)]
        for y in range(len(new_danger_map)):
            for x in range(len(new_danger_map)):
                old_y = y % len(danger_map)
                old_x = x % len(danger_map[0])

                inc_y = y // len(danger_map)
                inc_x = x // len(danger_map[0])

                inc_tot = inc_y + inc_x

                i = (danger_map[old_y][old_x] + inc_tot)
                if i >= 10:
                    i+= 1
                new_danger_map[y][x] = i % 10
        
        # small_map = [[0 for _ in range(5)] for _ in range(5)]
        # for y in range(0, len(new_danger_map), len(danger_map)):
        #     for x in range(0, len(new_danger_map), len(danger_map)):
        #         small_map[y//len(danger_map)][x//len(danger_map)] = new_danger_map[y][x]
            
        # for l in small_map:
        #     print(''.join([str(i) for i in l]))
        
        return bfs_priority((0, 0), (len(new_danger_map) -1, len(new_danger_map[0]) - 1), new_danger_map)


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
