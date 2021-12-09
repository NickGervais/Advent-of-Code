### Day 20: Jurassic Jigsaw ###

import copy
import re
import numpy as np

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
                cur_tile.append([c for c in line])

    tiles[cur_tile_id] = np.array(cur_tile)

# print(tiles)

def get_tile(all_tiles, tile_id, rotation, flip):
    tile = np.rot90(all_tiles[tile_id], rotation)
    if flip:
        tile = np.flip(tile, 1)
    return tile

def isValid(all_tiles: dict, board: list, tile_id: int, rotation: int, flip: bool, pos: tuple):
    tile = get_tile(all_tiles, tile_id, rotation, flip)
    
    top, right, bot, left = [tuple(map(sum, zip(x, pos))) for x in [(-1, 0), (0, 1), (1, 0), (0, -1)]]
    # check top
    if 0 <= top[0] < len(board) and 0 <= top[1] < len(board) and board[top[0]][top[1]] != (0, 0, None):
        cur_tile_id, cur_rot, cur_flip = board[top[0]][top[1]]
        cur_tile = get_tile(all_tiles, cur_tile_id, cur_rot, cur_flip)
        # print('check top: ', top, cur_tile_id)

        if not np.array_equal(cur_tile[-1,:], tile[0,:]):
            return False
    # check right
    if 0 <= right[0] < len(board) and 0 <= right[1] < len(board) and board[right[0]][right[1]] != (0, 0, None):
        cur_tile_id, cur_rot, cur_flip = board[right[0]][right[1]]
        cur_tile = get_tile(all_tiles, cur_tile_id, cur_rot, cur_flip)
        # print('check right: ', right, cur_tile_id)

        if not np.array_equal(cur_tile[:,0], tile[:,-1]):
            return False
    # check bottom
    if 0 <= bot[0] < len(board) and 0 <= bot[1] < len(board) and board[bot[0]][bot[1]] != (0, 0, None):
        cur_tile_id, cur_rot, cur_flip = board[bot[0]][bot[1]]
        cur_tile = get_tile(all_tiles, cur_tile_id, cur_rot, cur_flip)
        # print('check bot: ', bot, cur_tile_id)

        if not np.array_equal(cur_tile[0,:], tile[-1,:]):
            return False
    # check left
    if 0 <= left[0] < len(board) and 0 <= left[1] < len(board) and board[left[0]][left[1]] != (0, 0, None):
        cur_tile_id, cur_rot, cur_flip = board[left[0]][left[1]]
        cur_tile = get_tile(all_tiles, cur_tile_id, cur_rot, cur_flip)
        # print('check left: ', left, cur_tile_id)

        if not np.array_equal(cur_tile[:,-1], tile[:,0]):
            return False
    return True

def solve(all_tiles: dict, board: list, remaining_tiles: dict, remaining_positions):
    if len(remaining_positions) == 0:
        return True

    pos_to_check = remaining_positions[0]
    for tile_id, tile in remaining_tiles.items():
        for rotation in [0, 1, 2, 3]:
            for flip in [False, True]:
                # print(pos_to_check, tile_id, rotation, flip)
                if isValid(all_tiles, board, tile_id, rotation, flip, pos_to_check):
                    board[pos_to_check[0]][pos_to_check[1]] = (tile_id, rotation, flip)
                    remaining_tiles.pop(tile_id)
                    remaining_positions = remaining_positions[1:]

                    # print_board(board)

                    if solve(all_tiles, board, copy.deepcopy(remaining_tiles), copy.deepcopy(remaining_positions)):
                        return True
                    
                    board[pos_to_check[0]][pos_to_check[1]] = (0, 0, None)
                    remaining_tiles[tile_id] = tile
                    remaining_positions = [pos_to_check] + remaining_positions
                # print('\n')
    return False

def print_tile(tile):
    for row in tile:
        print(''.join([i for i in row]))
    print('\n')

def print_board(board):
    for row in board:
        print(row)

def part_1(tiles):
    # [(2311, 1, True), (1427, 1, True)]
    # [(1951, 1, True), (2729, 1, True)]
    # board = [[(0, 0, None)] * 2 for _ in range(2)]
    # board[0][0] = (2311, 1, True)
    # board[1][0] = (1951, 1, True)
    # board[0][1] = (1427, 1, True)
    # print_tile(get_tile(tiles, 1951, 1, True))
    # print_tile(get_tile(tiles, 1427, 1, True))
    # print_tile(get_tile(tiles, 2729, 1, True))
    # print(isValid(tiles, board, 2729, 1, True, (1, 1)))

    # new_tiles = {}
    # for i, t in tiles.items():
    #     if i in [1951, 2311, 2729, 1427]:
    #         new_tiles[i] = t

    n = int(np.sqrt(len(tiles)))
    board = [[(0, 0, None)] * n for _ in range(n)]

    remaining_tiles = copy.deepcopy(tiles)
    remaining_positions = []
    for x in range(len(board)):
        for y in range(len(board)):
            remaining_positions.append((x, y))

    if solve(tiles, board, remaining_tiles, remaining_positions) is False:
        print("No Solution")
    
    print_board(board)
    print(np.prod([t for t, _, _ in np.array(board)[[0, 0, -1, -1], [0, -1, 0, -1]]]))


part_1(tiles)














# tile_borders = {}
# for tile_id, tile_rows in tiles.items():
#     top = tile_rows[0]
#     right = ''.join([row[-1] for row in tile_rows])
#     bottom = tile_rows[-1]
#     left = ''.join([row[0] for row in tile_rows])
#     tile_borders[tile_id] = [top, right, bottom, left]

# border_matches = {}
# for tile_id, tile_borders in tile_borders.items():
#     # cube_swaps[idx1] = cube_swaps.setdefault(idx1, 0) + 1
#     for i, tile_border in enumerate(tile_borders):
#         border_matches.setdefault(tile_border, []).append((tile_id, i))

# print(border_matches, '\n')

# border_count = {}
# for border, tile_ids in border_matches.items():
#     if len(tile_ids) == 1:
#         for tile_id, side_id in tile_ids:
#             border_count[tile_id] = border_count.setdefault(tile_id, 0) + 1

# print(border_count)