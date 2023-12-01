import os
from aoc_utils import aoc_utils
from collections import defaultdict

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

item_values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_item_value(item):
    return item_values.index(item) + 1

def answer(problem_input, level, test=None):
    lines = []
    for line in problem_input.split('\n'):
        lines.append(line.strip())

    if level == 1 :
        item_priorities = []
        for l in lines:
            mid_index = int(len(l)/2)
            left, right = l[:mid_index], l[mid_index:]
            shared_item = (set(left).intersection(set(right))).pop()
            item_priorities.append(get_item_value(shared_item))
        return sum(item_priorities)
    elif level == 2:
        item_priorities = []

        for i in range(3, len(lines) + 1, 3):
            group = lines[i-3:i]
            shared_item = (set(group[0]) & set(group[1]) & set(group[2])).pop()
            item_priorities.append(get_item_value(shared_item))
        return sum(item_priorities)
            

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
