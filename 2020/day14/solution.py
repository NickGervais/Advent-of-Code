### Day 14: Docking Data ###

instructions = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        instructions.append(line.rstrip())

import re

def part_1(instructions):
    def apply_mask(mask, value):
        result = ''
        for i in reversed(range(len(mask))):
            num = mask[i]
            if num == 'X':
                result = value[i] + result
            else:
                result = num + result
        return result

    def process_mem(mem, mem_instructions, mask):
        for mem_idx, mem_val in mem_instructions:
            result = apply_mask(mask, mem_val)
            mem[mem_idx] = int(result, 2)
        return mem


    mem = {}
    cur_mask = 'X' * 36
    cur_mems_instructions = []
    for i in instructions:
        # print(i, cur_mask, cur_mems_instructions)
        if i.startswith('mask'):
            # process mem
            mem = process_mem(mem, cur_mems_instructions, cur_mask)

            # reset with new mask
            cur_mask = i.split(' = ')[1]
            cur_mems_instructions = []
        else:
            m, val = i.split(' = ')
            mem_idx = int(re.findall(r'\d+', m)[0])
            cur_mems_instructions.append((mem_idx, f'{int(val):036b}'))

    mem = process_mem(mem, cur_mems_instructions, cur_mask)

    result = 0
    for idx, value in mem.items():
        result += value
    return result

# print(part_1(instructions))
# solution: 5875750429995

import itertools

def part_2(instructions):
    def apply_mask_to_address(mask, address):
        result = ''
        for i in reversed(range(len(mask))):
            num = mask[i]
            if num == '0':
                result = address[i] + result
            else:
                result = num + result
        return result

    def process_mem(mem, mem_instructions, mask):
        for mem_address, mem_val in mem_instructions:
            result_address = apply_mask_to_address(mask, mem_address)

            x_indecies = []
            for i, char in enumerate(result_address):
                if char == 'X':
                    x_indecies.append(i)

            x_combinations = list(itertools.product([0, 1], repeat=len(x_indecies)))
            for combo in x_combinations:
                cur_address = list(result_address)
                for i, val in enumerate(combo):
                    cur_address[x_indecies[i]] = str(val)
                cur_address = ''.join(cur_address)
                mem[int(cur_address, 2)] = mem_val
        return mem

    mem = {}
    cur_mask = 'X' * 36
    cur_mems_instructions = []
    for i in instructions:
        if i.startswith('mask'):
            # process mem
            mem = process_mem(mem, cur_mems_instructions, cur_mask)

            # reset with new mask
            cur_mask = i.split(' = ')[1]
            cur_mems_instructions = []
        else:
            m, val = i.split(' = ')
            mem_idx = int(re.findall(r'\d+', m)[0])
            cur_mems_instructions.append((f'{int(mem_idx):036b}', int(val)))

    mem = process_mem(mem, cur_mems_instructions, cur_mask)

    result = 0
    for idx, value in mem.items():
        result += value
    return result

print(part_2(instructions))
# solution: 5272149590143