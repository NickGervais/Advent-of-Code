import os
from aoc_utils import aoc_utils
from collections import defaultdict
import math

year, day = os.getcwd().split('/')[-2:]
print(type(year), type(day))

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]


def get_first_digit(s: str) -> int:
    digits = iter([int(i) for i in s if i.isdigit()])
    return next(digits, None)


def get_first_digit_index(line: str) -> tuple:
    digits_index = iter([i for i, s in enumerate(line) if s.isdigit()])
    idx = next(digits_index, None)
    return idx, line[idx]


def get_last_digit_index(line: str) -> int:
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return i, line[i]
    return None


def get_first_word_digit(line: str) -> tuple:
    word_digits = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    smallest_index = float('inf')
    first_word_digit = None
    for word, digit in word_digits.items():
        idx = line.find(word)
        if idx == -1:
            continue
        if idx < smallest_index:
            smallest_index = idx
            first_word_digit = digit

    return smallest_index, first_word_digit


def get_last_word_digit(line: str) -> tuple:
    word_digits = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    largest_index = float('-inf')
    last_word_digit = None
    for word, digit in word_digits.items():
        try:
            idx = line.rindex(word)
        except Exception:
            continue
        if not idx:
            continue
        if idx > largest_index:
            largest_index = idx
            last_word_digit = digit

    return largest_index, last_word_digit


def answer(problem_input, level, test=None):
    lines = []
    for line in problem_input.split('\n'):
        lines.append(line.strip())

    if level == 1 :
        calibration_values = []
        for l in lines:
            a = get_first_digit(l)
            b = get_first_digit("".join(reversed(l)))
            calibration_values.append(int(f"{a}{b}"))
        return sum(calibration_values)
    elif level == 2:
        calibration_values = []
        for l in lines:
            i1, d1 = get_first_digit_index(l)
            i2, d2 = get_first_word_digit(l)
            if i1 < i2:
                a = d1
            else:
                a = d2

            i3, d3 = get_last_digit_index(l)
            i4, d4 = get_last_word_digit(l)
            if i3 > i4:
                b = d3
            else:
                b = d4

            cv = int(f"{a}{b}")
            calibration_values.append(cv)
        return sum(calibration_values)

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
