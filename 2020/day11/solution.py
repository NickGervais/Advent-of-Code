### Day 11: Seating System ###

seat_map = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        row = line.rstrip()
        seat_map.append([char for char in row])

def print_map(seat_map):
    for row in seat_map:
        print(''.join(row))
    print('\n')

def run_round(seat_map):
    total_changes = 0
    new_seat_map = []
    for i, row in enumerate(seat_map):
        new_row = []
        for j, char in enumerate(row):
            adjecent_occupied = 0
            # print('spot:', i, j)
            for a in [i-1, i, i+1]:
                for b in [j-1, j, j+1]:
                    if a < 0 or a >= len(row) or b < 0 or b >= len(row):
                        continue
                    elif a == i and b == j:
                        continue
                    else:
                        # print(a, b, seat_map[a][b])
                        if seat_map[a][b] == '#':
                            adjecent_occupied += 1
            if seat_map[i][j] == 'L' and adjecent_occupied == 0:
                new_row.append('#')
                total_changes += 1
            elif seat_map[i][j] == '#' and adjecent_occupied >= 4:
                new_row.append('L')
                total_changes += 1
            else:
                new_row.append(seat_map[i][j])
        # print(new_row)
        new_seat_map.append(new_row)
    return new_seat_map, total_changes

def part_1(seat_map):
    while True:
        seat_map, total_changes = run_round(seat_map)
        if total_changes == 0:
            break
    
    total_occupied = 0
    for row in seat_map:
        for char in row:
            if char == '#':
                total_occupied += 1
    print(total_occupied)

# part_1(seat_map)
# solution: 2468

def run_round_p2(seat_map):
    def out_of_range(x, y):
        if x < 0 or x >= len(seat_map[0]) or y < 0 or y >= len(seat_map):
            return True
        return False

    total_changes = 0
    new_seat_map = []
    for i, row in enumerate(seat_map):
        new_row = []
        for j, char in enumerate(row):
            first_occupied = 0
            # print('spot:', i, j)
            for dir_x in [-1, 0, 1]:
                for dir_y in [-1, 0, 1]:
                    if dir_x == 0 and dir_y == 0:
                        continue
                    cur_x = i + dir_x
                    cur_y = j + dir_y
                    while not out_of_range(cur_x, cur_y):
                        if seat_map[cur_x][cur_y] == '#':
                            first_occupied += 1
                            break
                        elif seat_map[cur_x][cur_y] == 'L':
                            break
                        else:
                            cur_x += dir_x
                            cur_y += dir_y
                    # print(cur_x, cur_y, last_seen)
            # print(first_occupied)
            if seat_map[i][j] == 'L' and first_occupied == 0:
                new_row.append('#')
                total_changes += 1
            elif seat_map[i][j] == '#' and first_occupied >= 5:
                new_row.append('L')
                total_changes += 1
            else:
                new_row.append(seat_map[i][j])
        # print(new_row)
        new_seat_map.append(new_row)
    return new_seat_map, total_changes


def part_2(seat_map):
    while True:
        seat_map, total_changes = run_round_p2(seat_map)
        # print_map(seat_map)
        if total_changes == 0:
            break
    
    total_occupied = 0
    for row in seat_map:
        for char in row:
            if char == '#':
                total_occupied += 1
    print(total_occupied)

part_2(seat_map)
# solution: 2214