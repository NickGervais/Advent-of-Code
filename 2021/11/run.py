import os
from aoc_utils import aoc_utils

year, day = os.getcwd().split('/')[-2:]

adj_cords = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def print_grid(grid):
    for i in grid:
        print(i)

def propogate_flashes(y, x, grid):
    grid[y][x] = -1
    for y1, x1 in adj_cords:
        cy, cx = y+y1, x+x1
        if 0 <= cy< len(grid) and 0 <= cx < len(grid[0]) and grid[cy][cx] != -1:
            grid[cy][cx] += 1
            if grid[cy][cx] > 9:
                propogate_flashes(cy, cx, grid)
    return

def answer(problem_input, level, test=None):
    grid = []
    for line in problem_input.split('\n'):
        grid.append([int(i) for i in line.strip()])

    if level == 1 or level == 2:
        total_flashes = 0
        i = 0
        in_sync = False
        while not in_sync:
            i += 1
            if i == 100:
                print('part 1:', total_flashes)

            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    grid[y][x] += 1
            
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] > 9:
                        propogate_flashes(y, x, grid)

            in_sync = True
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == -1:
                        total_flashes += 1
                        grid[y][x] = 0
                    else:
                        in_sync = False

        print('part 2:', i)
        return i

aoc_utils.run(answer, year=year, day=day)
