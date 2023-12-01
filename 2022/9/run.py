import os
from aoc_utils import aoc_utils
from collections import defaultdict
from typing import List, NamedTuple
from copy import copy

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def cords_are_attached_by_one(a: list, b: list) -> bool:
    if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1:
        return True
    else:
        return False  

def element_wise_addition(a: list, b: list) -> list:
    return [sum(value) for value in zip(a, b)]

def element_wise_subtraction(a: list, b: list) -> list:
    return [i - j for i, j in zip(a, b)]

def get_tail_delta(head: list, tail: list) -> list:
    delta = element_wise_subtraction(head, tail)
    new_delta = []
    for num in delta:
        if num > 0:
            # Positive number
            new_delta.append(1)
        elif num == 0:
            new_delta.append(0)
        else:
            # Negative number
            new_delta.append(-1)
    return new_delta

def move_knot(knot: list, delta: list) -> list:
    return element_wise_addition(knot, delta)

def move_tail_knot(head: list, tail: list):
    if not cords_are_attached_by_one(head, tail):
        # get tail delta then move it
        tail_delta = get_tail_delta(head, tail)
        tail = move_knot(tail, tail_delta)
    return head, tail

DELTAS = {
    'R': [1, 0],
    'L': [-1, 0],
    'D': [0, -1],
    'U': [0, 1]
}


def print_knots(knots: list):
    map = [['.' for _ in range(20)] for _ in range(20)]

    for i, cords in enumerate(knots):
        x, y = cords
        map[x][y] = str(i)

    for r in map:
        print(''.join(r))
    print()    



def answer(level):
    lines = []
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            lines.append(line.strip())

    if level == 1:
        knot_num = 2
    elif level == 2:
        knot_num = 10

    knots = [[0, 0] for _ in range(knot_num)]

    tail_has_been = set()
    tail_has_been.add('0_0')

    for line in lines:
        direction, amount = line.split(' ')
        head_delta = DELTAS[direction]
        for _ in range(int(amount)):
            knots[0] = move_knot(knots[0], head_delta)
            for i in range(1, len(knots)):
                head_i, tail_i = i-1, i
                knots[head_i], knots[tail_i] = move_tail_knot(knots[head_i], knots[tail_i])
                tail_has_been.add('_'.join([str(i) for i in knots[-1]]))

    return len(tail_has_been)

print(answer(2))
