### Day 13: Care Package###

## part 1 ##

import intcode

def partOne(outputs):
    i = 2
    num_blocks = 0
    while i < len(outputs):
        if outputs[i] == 2:
            num_blocks += 1
        i += 3

    return num_blocks

og_intcode = []
with open('input.txt', 'r') as problem_input:
    for i, line in enumerate(problem_input):
        og_intcode = [int(val) for val in line.split(",")]

intcode_comp = intcode.IntcodeComputer(list(og_intcode), 0)

outputs = []
while not intcode_comp.halted:
    outputs.append(intcode_comp.run_intcode(0))

print(partOne(outputs))

# Part Two

comp2 = intcode.IntcodeComputer(list(og_intcode), 0)
comp2.intcode[0] = 2

points = 0
ball_x = paddle_x = 0
input_val = 0
while not comp2.halted:
    x = comp2.run_intcode(input_val)
    y = comp2.run_intcode(input_val)
    tile_id = comp2.run_intcode(input_val)
    if not comp2.halted:
        ball_x = x if tile_id == 4 else ball_x
        paddle_x = x if tile_id == 3 else paddle_x
        points = tile_id if x == -1 and y == 0 else points
        input_val = (ball_x > paddle_x) - (ball_x < paddle_x)

print(points)
