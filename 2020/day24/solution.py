### Day 24: Lobby Layout ###

import re

paths = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        line = line.rstrip()
        paths.append(re.findall('(se|sw|e|w|ne|nw)', line))

dir_mult = {
    'ne': (0.5, 0.5),
    'e': (1, 0),
    'se': (0.5, -0.5),
    'nw': (-0.5, 0.5),
    'w': (-1, 0),
    'sw': (-0.5, -0.5)
}

def add_tuples(a, b):
    return tuple(map(sum, zip(a, b)))

def part_1(paths):
    flipped = {}
    for path in paths:
        pos = (0, 0)
        for direction in path:
            pos = add_tuples(pos, dir_mult[direction])
        
        if pos in flipped:
            flipped[pos] ^= 1
        else:
            flipped[pos] = 1
    
    num_black = 0
    for pos, col in flipped.items():
        if col % 2 == 1:
            num_black += 1

    print(num_black)

# part_1(paths)
# solution: 266

def get_adjacent_tiles(tile):
    return [add_tuples(tile, mult) for _, mult in dir_mult.items()]

def part_2(paths):
    def count_black_tiles(tile_state):
        num_black = 0
        for pos, col in tile_state.items():
            if col == 1:
                num_black += 1
        return num_black
    
    tile_state = {}
    for path in paths:
        pos = (0, 0)
        for direction in path:
            pos = add_tuples(pos, dir_mult[direction])
        
        # 0 = white, 1 = black
        if pos in tile_state:
            tile_state[pos] ^= 1  # toggle between 0 and 1
        else:
            tile_state[pos] = 1
    
    # run 100 days
    for day in range(100):
        next_state = {}
        possible_white_flips = {}
        for tile, col in tile_state.items():
            if col == 1:  # black tiles
                adjacent_blacks = 0
                for adjacent_tile in get_adjacent_tiles(tile):
                    if adjacent_tile in tile_state and tile_state[adjacent_tile] == 1:
                        adjacent_blacks += 1  # increment adjecent black tiles
                    else:
                        # count number of adjacent black tiles to all white tiles
                        possible_white_flips[adjacent_tile] = possible_white_flips.setdefault(adjacent_tile, 0) + 1
                        
                if adjacent_blacks == 0 or adjacent_blacks > 2:
                    next_state[tile] = 0  # flip to white
                else:
                    next_state[tile] = tile_state[tile]  # keep same
        
        for white_tile, count in possible_white_flips.items():
            if count == 2:
                # flip to black
                next_state[white_tile] = 1
        
        tile_state = next_state
        # print(f'Day {day + 1}: {count_black_tiles(tile_state)}')
    print(f'solution: {count_black_tiles(tile_state)}')

part_2(paths)
# solution: 3627

            
                