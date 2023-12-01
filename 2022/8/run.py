import os
from aoc_utils import aoc_utils
from collections import defaultdict
import numpy as np

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {
        'level': 1,
        'input': '''
            30373
            25512
            65332
            33549
            35390
        ''', 
        'output': '21'
    },
]

def print_map(map: list):
    for r in map:
        print(''.join([str(i) for i in r]))
    print()

def answer(level):
    forest = []
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            forest.append([int(i) for i in line.strip()])

    width = len(forest[0])
    height = len(forest)

    if level == 1:
        is_visible_map = [[0 for _ in range(width)] for _ in range(height)]

        print_map(forest)

        # from left
        highest = -1
        for r_idx in range(height):
            for c_idx in range(width):
                tree_height = forest[r_idx][c_idx]
                # print(f'{r_idx}_{c_idx}', tree_height, highest)
                if tree_height > highest:
                    highest = tree_height
                    is_visible_map[r_idx][c_idx] = 1
            highest = -1

        
        # from right
        highest = -1
        for r_idx in range(height):
            for c_idx in reversed(range(width)):
                tree_height = forest[r_idx][c_idx]
                if tree_height > highest:
                    highest = tree_height
                    is_visible_map[r_idx][c_idx] = 1
            highest = -1

        # from top
        highest = -1
        for c_idx in range(width):
            for r_idx in range(height):
                tree_height = forest[r_idx][c_idx]
                if tree_height > highest:
                    highest = tree_height
                    is_visible_map[r_idx][c_idx] = 1
            highest = -1
        
        # from bottom
        highest = -1
        for c_idx in range(width):
            for r_idx in reversed(range(height)):
                print(f'{r_idx}_{c_idx}', tree_height, highest)
                tree_height = forest[r_idx][c_idx]
                if tree_height > highest:
                    highest = tree_height
                    is_visible_map[r_idx][c_idx] = 1
            highest = -1

        print_map(is_visible_map)

        total_visible = 0
        for r in is_visible_map:
            for i in r:
                if i == 1:
                    total_visible += 1

        return total_visible
    elif level == 2:
        scenic_scores = [[[] for _ in range(width)] for _ in range(height)]

        for r_idx in range(height):
            for c_idx in range(width):
                tree_height = forest[r_idx][c_idx]

                n_idx = r_idx - 1
                s_score = 0
                while n_idx >= 0:
                    s_score += 1
                    if forest[n_idx][c_idx] >= tree_height:
                        break
                    n_idx -= 1
                scenic_scores[r_idx][c_idx].append(s_score)

                s_idx = r_idx + 1
                s_score = 0
                while s_idx < height:
                    s_score += 1
                    if forest[s_idx][c_idx] >= tree_height:
                        break
                    s_idx += 1
                scenic_scores[r_idx][c_idx].append(s_score)

                w_idx = c_idx - 1
                s_score = 0
                while w_idx >= 0:
                    s_score += 1
                    if forest[r_idx][w_idx] >= tree_height:
                        break
                    w_idx -= 1
                scenic_scores[r_idx][c_idx].append(s_score)
            
                e_idx = c_idx + 1
                s_score = 0
                while e_idx < width:
                    s_score += 1
                    if forest[r_idx][e_idx] >= tree_height:
                        break
                    e_idx += 1
                scenic_scores[r_idx][c_idx].append(s_score)

        max_scenic_score = -1
        for r in scenic_scores:
            for i in r:
                scenic_score = np.prod(i)
                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score

        return max_scenic_score

print(answer(2))