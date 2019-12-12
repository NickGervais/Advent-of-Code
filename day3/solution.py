### Day 3: Crossed Wires ###

def split_line(line: str) -> (str, int):
    return line[:1], int(line[1:])

def get_line_cordinates_set(origin: (int, int), direction: str, length: int, val_cords: dict) -> ((int, int), dict):
    cur_x, cur_y = origin
    if direction == 'R':
        for x in range(cur_x, cur_x + length + 1):
            val_cords[f'{x}_{cur_y}'] = len(val_cords)
        return (cur_x + length, cur_y), val_cords
    elif direction == 'L':
        for x in range(cur_x - length, cur_x + 1):
            val_cords[f'{x}_{cur_y}'] = len(val_cords)
        return (cur_x - length, cur_y), val_cords
    elif direction == 'U':
        for y in range(cur_y, cur_y + length + 1):
            val_cords[f'{cur_x}_{y}'] = len(val_cords)
        return (cur_x, cur_y + length), val_cords
    elif direction == 'D':
        for y in range(cur_y - length, cur_y + 1):
            val_cords[f'{cur_x}_{y}'] = len(val_cords)
        return (cur_x, cur_y - length), val_cords

def get_wire_cordinates_map(path: list) -> set:
    val_cords = {}
    cur_x = 0
    cur_y = 0
    for line in path:
        direction, length = split_line(line)
        (cur_x, cur_y), new_val_cords = get_line_cordinates_set((cur_x, cur_y), direction, length, val_cords)
        val_cords = new_val_cords
    return val_cords

def calc_manhattan_dist(x_1: int, y_1: int, x_2: int, y_2: int) -> int:
    x = abs(x_1 - x_2)
    y = abs(y_1 - y_2)
    return x + y

paths = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        paths.append([direction for direction in line.split(',')])

## Part 1 ##

path_1 = paths[0]
path_2 = paths[1]

val_cords_1 = get_wire_cordinates_map(path_1)
val_cords_2 = get_wire_cordinates_map(path_2)

cords_set_1 = set(val_cords_1.keys())
cords_set_2 = set(val_cords_2.keys())


intersections = cords_set_1.intersection(cords_set_2)
intersections.discard('0_0')
print(intersections)

dists = []
for cord in intersections:
    x, y = cord.split('_')
    x = int(x)
    y = int(y)
    dists.append(calc_manhattan_dist(0, 0, x, y))

print(min(dists))

## Part 2 ##

shortest_combined_dist = float('inf')

for cord in intersections:
    dist = val_cords_1[cord] + val_cords_2[cord]
    print(cord, dist)
    if dist < shortest_combined_dist:
        shortest_combined_dist = dist

print(shortest_combined_dist)