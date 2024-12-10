import os
from collections import defaultdict
from dataclasses import dataclass
import re

from pydantic import BaseModel, computed_field

from aoc_utils import aoc_utils


script_dir = os.path.dirname(os.path.abspath(__file__))
day = os.path.basename(script_dir)
year = os.path.basename(os.path.dirname(script_dir))


test_cases = [
    {'level': 1, 'input': '''3   4
4   3
2   5
1   3
3   9
3   3''', 'output': 11},
 {'level': 2, 'input': '''3   4
4   3
2   5
1   3
3   9
3   3''', 'output': 31},
]


class Day1(BaseModel):
    left_list: list[int]
    right_list: list[int]

    @computed_field
    @property
    def side_by_side_dif(self) -> int:
        a = sorted(self.left_list)
        b = sorted(self.right_list)

        dif_total = 0
        for i, _ in enumerate(a):
            dif_total += abs(a[i] - b[i])

        return dif_total

    @computed_field
    @property
    def similarity_score(self) -> int:

        score = 0
        for i in self.left_list:
            score += i * self.right_list.count(i)

        return score

    @classmethod
    def from_input_string(cls, input_string: str):
        left_list = []
        right_list = []
        for line in input_string.split('\n'):
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))
        return cls(left_list=left_list, right_list=right_list)


def answer(problem_input, level, test=None):
    d = Day1.from_input_string(problem_input)

    if level == 1:
        return d.side_by_side_dif

    elif level == 2:
        return d.similarity_score


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
