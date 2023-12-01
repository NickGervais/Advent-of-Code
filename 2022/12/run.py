import os
# from aoc_utils import aoc_utils
from collections import defaultdict
from typing import List, NamedTuple
from copy import copy
import math

year, day = os.getcwd().split('/')[-2:]


def element_wise_addition(a: tuple, b: tuple):
    return tuple([sum(x) for x in zip(a,b)])

def generate_adjecent_cords(cords: tuple):
    deltas = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    return [element_wise_addition(cords, d) for d in deltas]

def manhattan(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])



def astar(start, end, grid):
    fscores = {}
    gscores = {}
    previous = {}
    remaining = set()
    # for y in range(len(grid)):
    #     for x in range(len(grid[0])):
    #         weight = float('inf')
    #         if (y, x) == start:
    #             weight = 0

    #         path_weights[(y, x)] = weight
    #         remaining.add((y, x))
    #         previous[(y, x)] = None
    
    while len(remaining) > 0:
        # a = {cords: val for cords, val in path_weights.items() if cords in remaining}
        q = min(fscores, key=fscores.get)
        # weight = fscores[q]
        # y, x = n

        for next_cords in generate_adjecent_cords(q):
            y_next, x_next = next_cords
            if 0 <= y_next < len(grid) and 0 <= x_next < len(grid[0]):
                
                heuristic = math.sqrt((y_next - end[0])**2 + (x_next - end[1])**2)
                g = gscores[q] + abs(grid[q[0]][q[1]] - grid[y_next][x_next])
                f = g + heuristic
                if next_cords in fscores and f < fscores[next_cords]:
                    fscores[next_cords] = f
                    previous[next_cords] = q
        
        remaining.remove(q)

    return previous, fscores

def astarsearch(elevation_map: List[List[int]], start: tuple, target: tuple):
    fscores = {start: 0}
    open_cords_list = [start]
    closed_cords_list = []

    while len(open_cords_list) > 0:

        open_list.sort(key=lambda x: x['fscore'])
        q = open_list.pop(0)
        successors = generate_adjecent_cords(q['cords'])
        print("Q", q)

        for successor in successors:
            print("SUCCESSOR", successor)
            if successor == target:
                return open_list, closed_list
            
            elevation_change = abs(ord(elevation_map[q['cords'][0]][q['cords'][1]]) - ord(elevation_map[successor[0]][successor[1]]))
            g = q['gscore'] + elevation_change
            h = manhattan(successor, target)
            f = g + h

            position_has_shorter_path_in_open = next((True for i in open_list if i['cords'] == successor and i['fscore'] < f ), None)
            if position_has_shorter_path_in_open:
                continue
            position_has_shorter_path_in_closed = next((True for i in closed_list if i['cords'] == successor and i['fscore'] < f ), None)
            if position_has_shorter_path_in_closed:
                continue

            open_list.append({'cords': successor, 'gscore': g, 'fscore': f})
        
        closed_list.append(q)

    return open_list, closed_list




def answer(level):
    start_cords = None
    end_cords = None
    elevation_map = []
    ascii_grid = []
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            row = list(line.strip())
            for c_i, char_v in enumerate(row):
                if char_v == 'S':
                    start_cords = (i, c_i)
                elif char_v == 'E':
                    end_cords = (i, c_i)

            elevation_map.append(row)

    ascii_grid = [[0 for _ in range(len(elevation_map[0]))] for _ in range(len(elevation_map))]
    for yi, r in enumerate(elevation_map):
        print(r)
        for xi, char_v in enumerate(r):
            if char_v == 'S':
                ascii_grid[yi][xi] = 0
            elif char_v == 'E':
                ascii_grid[yi][xi] = 9999
            else:
                ascii_grid[yi][xi] = ord(char_v)

    print(start_cords)
    print(end_cords)

    for r in ascii_grid:
        print(r)

    print(astar(start_cords, end_cords, ascii_grid))

print(answer(1))