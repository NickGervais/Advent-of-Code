import os
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
import operator
import re
from typing import ClassVar

from pydantic import BaseModel

from aoc_utils import aoc_utils
from itertools import product


script_dir = os.path.dirname(os.path.abspath(__file__))
day = os.path.basename(script_dir)
year = os.path.basename(os.path.dirname(script_dir))


test_cases = [
    {'level': 1, 'input': '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20''', 'output': 3749},
    {'level': 2, 'input': '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20''', 'output': 11387},
]


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))

def add(a: int, b: int) -> int:
    return a + b

def mul(a: int, b: int) -> int:
    return a * b


class Operators(Enum):
    ADD = add
    MUL = mul
    CAT = concat


class Equation(BaseModel):
    test_value: int
    numbers: list[int]

    def find_valid_equation_operators(self, valid_operators: list) -> list | None:
        '''brute force'''
        operator_slot_count = len(self.numbers) - 1

        all_operator_combinations = list(product(valid_operators, repeat=operator_slot_count))

        for operator_combination in all_operator_combinations:
            result = self.numbers[0]
            for i, o in enumerate(operator_combination):
                result = o(result, self.numbers[i + 1])
            if result == self.test_value:
                return list(operator_combination)

        return None

    @classmethod
    def from_str_line(cls, line: str):
        test_value_str, numbers_str = line.split(':')
        test_value = int(test_value_str)
        numbers = list(map(int, re.findall(r'\d+', numbers_str)))
        return cls(test_value=test_value, numbers=numbers)


class Day7(BaseModel):
    equations: list[Equation]
    part_1_valid_operators: ClassVar[list] = [Operators.ADD, Operators.MUL]
    part_2_valid_operators: ClassVar[list] = [Operators.ADD, Operators.MUL, Operators.CAT]

    def part_1(self) -> int:
        total = 0
        for equation in self.equations:
            if equation.find_valid_equation_operators(self.part_1_valid_operators):
                total += equation.test_value
        return total

    def part_2(self) -> int:
        total = 0
        for equation in self.equations:
            if equation.find_valid_equation_operators(self.part_2_valid_operators):
                total += equation.test_value
        return total

    @classmethod
    def from_input_str(cls, input_str: str):
        equations = []
        for line in input_str.split('\n'):
            equations.append(Equation.from_str_line(line))
        return cls(equations=equations)


def answer(problem_input, level, test=None):
    d = Day7.from_input_str(problem_input)

    if level == 1:
        return d.part_1()

    elif level == 2:
        return d.part_2()


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
