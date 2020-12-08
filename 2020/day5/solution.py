### Day 5: Binary Boarding ###
import math

seat_sequences = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        seat_sequences.append(line.rstrip())

def get_seat_id(sequence):
    row_seq = sequence[:7]
    col_seq = sequence[7:]

    x_row = 0
    y_row = 127
    for char in row_seq:
        diff = int((y_row - x_row) / 2)
        if char == 'F':
            y_row = x_row + diff
        elif char == 'B':
            x_row = y_row - diff
    row = x_row if char == 'F' else y_row

    x_col = 0
    y_col = 7
    for char in col_seq:
        diff = int((y_col - x_col) / 2)
        if char == 'L':
            y_col = x_col + diff
        elif char == 'R':
            x_col = y_col - diff
    col = x_col if char == 'L' else y_col

    seat_id = (row * 8) + col
    return row, col, seat_id

def part_1():
    max_seat_id = 0
    for sequence in seat_sequences:
        row, col, seat_id = get_seat_id(sequence)

        if seat_id > max_seat_id:
            max_seat_id = seat_id
    
    return max_seat_id

# print(part_1())
# solution: 980

def part_2():
    seat_ids = []
    for sequence in seat_sequences:
        row, col, seat_id = get_seat_id(sequence)
        seat_ids.append(seat_id)
    
    
    previous_seat_id = 0
    seat_ids.sort()
    for seat_id in seat_ids:
        if seat_id - previous_seat_id == 2:
            print(previous_seat_id + 1)
        previous_seat_id = seat_id
    
part_2()
# solution: 607