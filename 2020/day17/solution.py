### Day 17: Conway Cubes ###

active_indexes = set()
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        for j, char in enumerate(line.rstrip()):
            if char == '#':
                active_indexes.add((0, 0, i, j))


def adject_cubes_3d(z, y, x):
    indexes = []
    for z_i in [z-1, z, z+1]:
        for y_i in [y-1, y, y+1]:
            for x_i in [x-1, x, x+1]:
                if (z_i, y_i, x_i) != (z, y, x):
                    indexes.append((z_i, y_i, x_i))
    return indexes

def run_cycle(active_indexes, adject_cubes_func):
    cube_swaps = {} # key = index tuple, value = number adjecent active
    # print(active_indexes)

    for idx in list(active_indexes):
        neighbors = adject_cubes_func(*idx)
        for idx1 in neighbors:
            cube_swaps[idx1] = cube_swaps.setdefault(idx1, 0) + 1

    new_active_indexes = set()
    for idx, val in cube_swaps.items():
        if idx in active_indexes and val in [2, 3]:
            # print('active', idx, val)
            new_active_indexes.add(idx)
        elif idx not in active_indexes and val == 3:
            # print('inactive', idx, val)
            new_active_indexes.add(idx)
    
    return new_active_indexes

def part_1(active_indexes):
    for _ in range(6):
        active_indexes = run_cycle(active_indexes, adject_cubes_3d)
    print(len(active_indexes))

# part_1(active_indexes)
# solution: 448


def adject_cubes_4d(w, z, y, x):
    indexes = []
    for w_i in [w-1, w, w+1]:
        for z_i in [z-1, z, z+1]:
            for y_i in [y-1, y, y+1]:
                for x_i in [x-1, x, x+1]:
                    if (w_i, z_i, y_i, x_i) != (w, z, y, x):
                        indexes.append((w_i, z_i, y_i, x_i))
    return indexes

def adject_cubes(dem, idx):
    indexes = []
    for i in dem:
        
    for w_i in [w-1, w, w+1]:
        for z_i in [z-1, z, z+1]:
            for y_i in [y-1, y, y+1]:
                for x_i in [x-1, x, x+1]:
                    if (w_i, z_i, y_i, x_i) != (w, z, y, x):
                        indexes.append((w_i, z_i, y_i, x_i))
    return indexes

def part_2(active_indexes):
    for _ in range(6):
        active_indexes = run_cycle(active_indexes, adject_cubes_4d)
    print(len(active_indexes))

part_2(active_indexes)
# solution: 2400
