### Day 20: Jurassic Jigsaw ###

import re

tiles = {}
cur_tile_id = None
cur_tile = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        line = line.rstrip()
        if not line or line.isspace():
            tiles[cur_tile_id] = cur_tile
            cur_tile_id = None
            cur_tile = []
        else:
            match_group = re.match(r'^Tile ([0-9]{4}):$', line)
            if match_group:
                cur_tile_id = int(match_group.group(1))
            else:
                cur_tile.append(line)

    tiles[cur_tile_id] = cur_tile

tile_borders = {}
for tile_id, tile_rows in tiles.items():
    top = tile_rows[0]
    right = ''.join([row[-1] for row in tile_rows])
    bottom = tile_rows[-1]
    left = ''.join([row[0] for row in tile_rows])
    tile_borders[tile_id] = [top, right, bottom, left]

border_matches = {}
for tile_id, tile_borders in tile_borders.items():
    # cube_swaps[idx1] = cube_swaps.setdefault(idx1, 0) + 1
    for i, tile_border in enumerate(tile_borders):
        border_matches.setdefault(tile_border, []).append((tile_id, i))

print(border_matches, '\n')

border_count = {}
for border, tile_ids in border_matches.items():
    if len(tile_ids) == 1:
        for tile_id, side_id in tile_ids:
            border_count[tile_id] = border_count.setdefault(tile_id, 0) + 1

print(border_count)