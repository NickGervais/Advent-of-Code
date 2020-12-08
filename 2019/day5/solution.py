### Day 5: Sunny with a Chance of Asteroids ###

opcode_params = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    99: 0
}

def read_instruction(inst: int) -> (int, list):
    """
    :returns: (opcode, mode per parameter)
    """
    inst = str(inst)
    opcode = int(inst[-2:])
    inst = inst[:-2]

    modes = []
    for i in range(opcode_params[opcode]):
        if inst == '':
            modes.append(0)
        else:
            modes.append(int(inst[-1:]))
            inst = inst[:-1]
    return opcode, modes

def get_val(intcode: list, param: int, mode: int) -> int:
    if mode == 0:
        return intcode[param]
    elif mode == 1:
        return param


def process_intcode_at_pos(intcode: list, pos: int) -> (bool, list, int):
    """
    :returns: (if it has ended, the new intcode, the new instruction pointer position)
    """
    opcode, modes = read_instruction(intcode[pos])
    
    if opcode == 1: # add
        param_1, mode_1 = intcode[pos + 1], modes[0]
        param_2, mode_2 = intcode[pos + 2], modes[1]
        param_3, mode_3 = intcode[pos + 3], modes[2]

        val_1 = get_val(intcode, param_1, mode_1)
        val_2 = get_val(intcode, param_2, mode_2)

        if mode_3 == 0:
            intcode[param_3] = val_1 + val_2
        elif mode_3 == 1:
            incode[pos + 3] = val_1 + val_2

        return False, intcode, pos + 4

    elif opcode == 2: # multiply
        param_1, mode_1 = intcode[pos + 1], modes[0]
        param_2, mode_2 = intcode[pos + 2], modes[1]
        param_3, mode_3 = intcode[pos + 3], modes[2]

        val_1 = get_val(intcode, param_1, mode_1)
        val_2 = get_val(intcode, param_2, mode_2)

        if mode_3 == 0:
            intcode[param_3] = val_1 * val_2
        elif mode_3 == 1:
            intcode[pos + 3] = val_1 * val_2

        return False, intcode, pos + 4

    elif opcode == 3: # input
        param_1, mode_1 = intcode[pos + 1], modes[0]
        value = input("opcode 3 input: ")
        value = int(value)

        if mode_1 == 0:
            intcode[param_1] = value
        elif mode_1 == 1:
            intcode[pos + 1] = value
        return False, intcode, pos + 2

    elif opcode == 4: # output
        param_1, mode_1 = intcode[pos + 1], modes[0]
        
        if mode_1 == 0:
            value = intcode[param_1]
        elif mode_1 == 1:
            value = param_1
        print(f"opcode 4 output: {value}")
        return False, intcode, pos + 2

    elif opcode == 5: # jump-if-true
        param_1, mode_1 = intcode[pos + 1], modes[0]
        param_2, mode_2 = intcode[pos + 2], modes[1]

        val_1 = get_val(intcode, param_1, mode_1)
        val_2 = get_val(intcode, param_2, mode_2)
        if val_1 is not 0:
            pos = val_2
        else:
            pos = pos + 3
        return False, intcode, pos

    elif opcode == 6: # jump-if-false
        param_1, mode_1 = intcode[pos + 1], modes[0]
        param_2, mode_2 = intcode[pos + 2], modes[1]

        val_1 = get_val(intcode, param_1, mode_1)
        val_2 = get_val(intcode, param_2, mode_2)

        if val_1 is 0:
            pos = val_2
        else:
            pos = pos + 3
        return False, intcode, pos
    
    elif opcode == 7: # less than
        param_1, mode_1 = intcode[pos + 1], modes[0]
        param_2, mode_2 = intcode[pos + 2], modes[1]
        param_3, mode_3 = intcode[pos + 3], modes[2]

        val_1 = get_val(intcode, param_1, mode_1)
        val_2 = get_val(intcode, param_2, mode_2)
        
        if val_1 < val_2:
            val = 1
        else:
            val = 0

        if mode_3 == 0:
            intcode[param_3] = val
        elif mode_3 == 1:
            intcode[pos + 3] = val
        return False, intcode, pos + 4

    elif opcode == 8: # equals
        param_1, mode_1 = intcode[pos + 1], modes[0]
        param_2, mode_2 = intcode[pos + 2], modes[1]
        param_3, mode_3 = intcode[pos + 3], modes[2]

        val_1 = get_val(intcode, param_1, mode_1)
        val_2 = get_val(intcode, param_2, mode_2)
        
        if val_1 == val_2:
            val = 1
        else:
            val = 0
            
        if mode_3 == 0:
            intcode[param_3] = val
        elif mode_3 == 1:
            intcode[pos + 3] = val
        return False, intcode, pos + 4

    elif opcode == 99:
        return True, intcode, pos
    
    else:
        print('not a valid opcode')
        return None

def run_intcode(intcode: list):
    pointer = 0
    ended = False
    while not ended:
        ended, intcode, pointer = process_intcode_at_pos(intcode, pointer)


og_intcode = []
with open('input.txt', 'r') as problem_input:
    for i, line in enumerate(problem_input):
        og_intcode = [int(val) for val in line.split(",")]

## Part 1 ##

# cur_intcode = list(og_intcode)
# run_intcode(cur_intcode)

## Part 2 ##

cur_intcode = list(og_intcode)
run_intcode(cur_intcode)
