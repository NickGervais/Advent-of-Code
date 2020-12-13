### Day 12: Rain Risk ###

actions = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        actions.append(line.rstrip())


action_mults = {
    'N': [0, 1],
    'S': [0, -1],
    'E': [1, 0],
    'W': [-1, 0]
}

action_deg = {
    0: 'E',
    90: 'N',
    180: 'W',
    270: 'S',
    360: 'E'
}

def add_lists(l1, l2):
    return [sum(i) for i in zip(l1, l2)]

def mult_list(value, l):
    return [i * value for i in l]

def part_1(actions):
    cur_dir = 'E'
    cur_deg = 0
    cur_pos = [0, 0]

    for action in actions:
        direction = action[0]
        value = int(action[1:])
        if direction == 'F':
            cur_pos = add_lists(cur_pos, mult_list(value, action_mults[cur_dir]))
        elif direction == 'L':
            cur_deg = (cur_deg + value) % 360
            cur_dir = action_deg[cur_deg]
        elif direction == 'R':
            cur_deg = (cur_deg - value) % 360
            cur_dir = action_deg[cur_deg]
        elif direction in ['N', 'S', 'E', 'W']:
            cur_pos = add_lists(cur_pos, mult_list(value, action_mults[direction]))
            
    return sum([abs(i) for i in cur_pos])

# print(parts_1(actions))
# solution: 319

import math

def rotate_origin_only(xy, radians):
    x, y = xy
    xx = x * math.cos(radians) + y * math.sin(radians)
    yy = -x * math.sin(radians) + y * math.cos(radians)

    return [round(xx), round(yy)]

def part_2(actions):
    waypoint = [10, 1]
    cur_pos = [0, 0]

    for action in actions:
        direction = action[0]
        value = int(action[1:])
        if direction == 'F':
            cur_pos = add_lists(cur_pos, mult_list(value, waypoint))
        elif direction == 'L':
            waypoint = rotate_origin_only(waypoint, math.radians(-value))
        elif direction == 'R':
            waypoint = rotate_origin_only(waypoint, math.radians(value))
        elif direction in ['N', 'S', 'E', 'W']:
            waypoint = add_lists(waypoint, mult_list(value, action_mults[direction]))

    return sum([abs(i) for i in cur_pos])

print(part_2(actions))
# solution: 50157