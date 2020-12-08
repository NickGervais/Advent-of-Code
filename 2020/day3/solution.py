### Day 3: Toboggan Trajectory ###
import numpy

def part_1(x_mult, y_mult):
    forest = []
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            line = line.rstrip()
            forest.append(list(line))
    
    # first spot (0, 0) is guarentee not a tree
    x = x_mult
    y = y_mult

    hit_trees = 0

    while y < len(forest):
        x_cord = x % len(forest[0])
        
        if forest[y][x_cord] == '#':
            hit_trees += 1
        
        x = x + x_mult
        y = y + y_mult

    return hit_trees

print(part_1(3, 1))
# solution: 254

def part_2():
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    hit_trees = []
    for slope in slopes:
        hit_trees.append(part_1(*slope))
    
    return numpy.prod(hit_trees)

print(part_2())
# solution: 1666768320