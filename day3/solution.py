### Day 3: Crossed Wires ###

def split_line(line: str) -> (str, int):
    return line[:1], int(line[1:])

def get_line_cordinates_set(origin: (int, int), direction: str, length: int) -> ((int, int), str):
    cur_x, cur_y = origin
    if direction == 'R':
        return (cur_x + length, cur_y), set([f'{x}_{cur_y}' for x in range(cur_x, cur_x + length + 1)])
    elif direction == 'L':
        return (cur_x - length, cur_y), set([f'{x}_{cur_y}' for x in range(cur_x - length, cur_x + 1)])
    elif direction == 'U':
        return (cur_x, cur_y + length), set([f'{cur_x}_{y}' for y in range(cur_y, cur_y + length + 1)])
    elif direction == 'D':
        return (cur_x, cur_y - length), set([f'{cur_x}_{y}' for y in range(cur_y - length, cur_y + 1)])

def get_wire_cordinates_set(path: list) -> set:
    cords = set()
    cur_x = 0
    cur_y = 0
    for line in path:
        direction, length = split_line(line)
        (cur_x, cur_y), new_cords = get_line_cordinates_set((cur_x, cur_y), direction, length)
        cords.update(new_cords)
    return cords

def calc_manhattan_dist(x_1: int, y_1: int, x_2: int, y_2: int) -> int:
    x = abs(x_1 - x_2)
    y = abs(y_1 - y_2)
    return x + y

paths = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        paths.append([direction for direction in line.split(',')])

path_1 = paths[0]
path_2 = paths[1]

cords_1 = get_wire_cordinates_set(path_1)
cords_2 = get_wire_cordinates_set(path_2)

intersections = cords_1.intersection(cords_2)
intersections.discard('0_0')

dists = []
for cord in intersections:
    x, y = cord.split('_')
    x = int(x)
    y = int(y)
    dists.append(calc_manhattan_dist(0, 0, x, y))

print(min(dists))

## Part 2 ##