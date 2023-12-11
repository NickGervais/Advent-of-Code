import os
from aoc_utils import aoc_utils
from collections import defaultdict
from dataclasses import dataclass
import re

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45''', 'output': 114},
    {'level': 2, 'input': '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45''', 'output': 2},
]


def reduce_sequence(l: list) -> list:
    sequences = [l]

    while not all(s == 0 for s in sequences[-1]):
        new_sequence = []
        for i in range(1, len(sequences[-1])):
            val1 = sequences[-1][i-1]
            val2 = sequences[-1][i]
            new_sequence.append(sequences[-1][i] - sequences[-1][i-1])
        sequences.append(new_sequence)

    return sequences


def back_propogate(sequences: list) -> list:
    sequences[-1].append(0)
    for i in reversed(range(1, len(sequences))):
        val1 = sequences[i-1][-1]
        val2 = sequences[i][-1]
        next_val = val1 + val2
        sequences[i-1].append(next_val)

    return sequences


def back_propogate_back(sequences: list) -> list:
    sequences[-1].insert(0, 0)

    for i in reversed(range(1, len(sequences))):
        val1 = sequences[i-1][0]
        val2 = sequences[i][0]
        next_val = val1 - val2
        sequences[i-1].insert(0, next_val)

    return sequences


def answer(problem_input, level, test=None):

    lines = []
    for line in problem_input.split('\n'):
        line = list(map(int, line.strip().split(' ')))
        lines.append(line)

    if level == 1:
        s = 0
        for line in lines:
            sequences = reduce_sequence(line)
            sequences = back_propogate(sequences)
            s += sequences[0][-1]
        return s

    elif level == 2:
        s = 0
        for line in lines:
            sequences = reduce_sequence(line)
            sequences = back_propogate_back(sequences)
            s += sequences[0][0]
        return s


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
