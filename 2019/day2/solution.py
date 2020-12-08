### Day 2: 1202 Program Alarm ###

def process_intcode_at_pos(intcode: list, pos: int) -> (bool, list, int):
    """
    :returns: (if it has ended, the new intcode, the new instruction pointer position)
    """
    opcode = intcode[pos]
    
    if opcode == 1: # add
        pos_a = intcode[pos + 1]
        pos_b = intcode[pos + 2]
        pos_overwrite = intcode[pos + 3]

        val_a = intcode[pos_a]
        val_b = intcode[pos_b]
        intcode[pos_overwrite] = val_a + val_b

        return False, intcode, pos + 4

    elif opcode == 2: # multiply
        pos_a = intcode[pos + 1]
        pos_b = intcode[pos + 2]
        pos_overwrite = intcode[pos + 3]

        val_a = intcode[pos_a]
        val_b = intcode[pos_b]
        intcode[pos_overwrite] = val_a * val_b
        return False, intcode, pos + 4

    elif opcode == 99:
        return True, intcode, pos
    
    else:
        print('not a valid opcode')
        return None

og_intcode = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        og_intcode = [int(val) for val in line.split(",")]
        
## Part 1: ##
# intcode = list(og_intcode)
# intcode[1] = 12
# intcode[2] = 2

# pointer = 0
# ended = False
# while not ended:
#     ended, intcode, pointer = process_intcode_at_pos(intcode, pointer)

# print(intcode)

## Part 2 ##

for i in range(99):
    for j in range(99):
        cur_intcode = list(og_intcode)
        cur_intcode[1] = i
        cur_intcode[2] = j

        pointer = 0
        ended = False
        while not ended:
            ended, cur_intcode, pointer = process_intcode_at_pos(cur_intcode, pointer)
        if cur_intcode[0] == 19690720:
            print(100 * i + j)

