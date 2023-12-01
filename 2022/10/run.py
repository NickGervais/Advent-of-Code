import os
from aoc_utils import aoc_utils
from collections import defaultdict
from typing import List, NamedTuple
from copy import copy

year, day = os.getcwd().split('/')[-2:]

def answer(level):
    lines = []
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            lines.append(line.strip())

    signal_strength = 0
    x_register = 1
    cycles = 0

    crt = []
    for instruction in lines:
        match instruction.split(' '):
            case['noop']:
                if cycles % 40 in [x_register -1, x_register, x_register+1]:
                    crt.append('#')
                else:
                    crt.append('.')
                cycles += 1

                # part 1
                if cycles in [20, 60, 100, 140, 180, 220]:
                    signal_strength += cycles * x_register

            case['addx', value]:
                # two cycles
                for _ in range(2):
                    if cycles % 40 in [x_register -1, x_register, x_register+1]:
                        crt.append('#')
                    else:
                        crt.append('.')
                    cycles += 1

                    # part 1
                    if cycles in [20, 60, 100, 140, 180, 220]:
                        signal_strength += cycles * x_register
                x_register += int(value)

    for i in range(39, len(crt), 40):
        print(''.join(crt[i-39:i+1]))

    return signal_strength

print(answer(1))