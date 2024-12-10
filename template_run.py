import os
from collections import defaultdict
from dataclasses import dataclass
import re

from pydantic import BaseModel

from aoc_utils import aoc_utils


script_dir = os.path.dirname(os.path.abspath(__file__))
day = os.path.basename(script_dir)
year = os.path.basename(os.path.dirname(script_dir))


test_cases = [
    # {'level': 1, 'input': '''''', 'output': ''},
]


def answer(problem_input, level, test=None):
    lines = []
    for line in problem_input.split('\n'):
        line = line.strip()
        lines.append(line)

    if level == 1:
        return 0

    elif level == 2:
        return 0


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
