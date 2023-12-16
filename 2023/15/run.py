import os
from aoc_utils import aoc_utils
from collections import defaultdict
from typing import Dict, List, Tuple

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7''', 'output': 1320},
    {'level': 2, 'input': '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7''', 'output': 145},
]


def get_hash_value(label: str) -> int:
    cur_value = 0
    for char in label:
        ascii_value = ord(char)
        cur_value += ascii_value
        cur_value *= 17
        cur_value %= 256
    return cur_value


def answer(problem_input, level, test=None):
    values = []
    for value in problem_input.split(','):
        value = value.strip()
        values.append(value)

    if level == 1:
        final_value = 0
        for value in values:
            final_value += get_hash_value(value)
        return final_value

    elif level == 2:
        hashmap: Dict[int, List[Tuple[str, int]]] = defaultdict(list)
        for value in values:
            if '-' in value:
                label, _ = value.split('-')
                box = get_hash_value(label)
                lens_locations = [i for i, lens in enumerate(hashmap[box]) if lens[0] == label]

                for i in reversed(lens_locations):
                    hashmap[box].pop(i)

            elif '=' in value:
                label, focal_length = value.split('=')
                box = get_hash_value(label)
                lens_locations = [i for i, lens in enumerate(hashmap[box]) if lens[0] == label]

                if len(lens_locations) == 1:
                    hashmap[box][lens_locations[0]] = (label, focal_length)
                else:
                    hashmap[box].append((label, focal_length))

            # print(hashmap)

        focal_power = 0
        for box, lenses in hashmap.items():
            for i, lens in enumerate(lenses):
                focal_power += (box + 1) * (i + 1) * int(lens[1])
        return focal_power


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
