### Day 10: Monitoring Station ###
import math

def calc_angle(x1: int, y1: int, x2: int, y2: int) -> float:
    degs = math.degrees(math.atan2((y2 - y1), (x2 - x1)))
    degs = degs + 90
    if degs < 0:
        degs = degs + 360

    return degs

def get_astroid_cords(map: list) -> list:
    astroid_cords = []
    for x in range(len(map)):
        for y in range(len(map)):
            space = map[x][y]
            if space == '#':
                astroid_cords.append((x, y))
    return astroid_cords

def read_input() -> list:
    map = []
    with open('input.txt', 'r') as f:
        for _, line in enumerate(f):
            line = line.rstrip()
            row = []
            for char in line:
                row.append(char)
            map.append(row)
    return map


## Part One ##
astroid_map = read_input()
astroid_cords = get_astroid_cords(astroid_map)

angle_map = {}
for x, y in astroid_cords:
    angle_map[(x, y)] = {}
    for x2, y2 in astroid_cords:
        if x == x2 and y == y2:
            continue    # skip yourself
        angle = calc_angle(x, y, x2, y2)
        if angle not in angle_map[(x, y)]:
            angle_map[(x, y)][angle] = [(x2, y2)]
        else:
            angle_map[(x, y)][angle].append((x2, y2))

best_astroid = None
astroid_count = 0
for astroid, angles in angle_map.items():
    if len(angles) >= astroid_count:
        best_astroid = astroid
        astroid_count = len(angles)

print(best_astroid)
print(astroid_count)

## Part Two - Vaporizing astroids ##
# What's the 200th astroid vaporized

def vaporize_closest(x1:int, y1: int, astroids: list) -> list:
    closest = astroids[0]
    closest_dist = float('inf')
    for astroid in astroids[0:]:
        x = x1 - astroid[0]
        y = y1 - astroid[1]
        dist = math.sqrt((x*x) + (y*y))
        if dist < closest_dist:
            closest_dist = dist
            closest = astroid
    
    astroids.remove(closest)
    return closest, astroids

angles = angle_map[best_astroid]
sorted_angles = list(angles.keys())
sorted_angles.sort()

vaporized_count = 0
vaporized_cords = None
not_found = True
while not_found:
    for angle in sorted_angles:
        if len(angles[angle]) > 0:
            cords, angles[angle] = vaporize_closest(best_astroid[0], best_astroid[1], angles[angle])
            vaporized_count += 1
            # print(vaporized_count, cords)
            if vaporized_count == 200:
                vaporized_cords = cords
                not_found = False
                break

print(vaporized_cords[0] * 100 + vaporized_cords[1])

# a = [(4, 2), (3, 2), (5, 2)]
# # print(vaporize_closest(2, 2, a))

# print(calc_angle(2, 2, 2, 0))
# print(calc_angle(2, 2, 4, 0))
# print(calc_angle(2, 2, 4, 2))
# print(calc_angle(2, 2, 4, 4))




