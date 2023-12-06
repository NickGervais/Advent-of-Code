import os
from aoc_utils import aoc_utils
import math
from typing import List, Dict
import re
from dataclasses import dataclass


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
    {
        'level': 1,
        'input': """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""",
        "output": 4361
    },
    {
        'level': 2,
        'input': """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""",
        "output": 467835
    },
]


@dataclass
class Cord:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


@dataclass
class NumberCords:
    value: int
    start: Cord
    end: Cord

    def cord_hit(self, cord: Cord) -> bool:
        x_hit = self.start.x <= cord.x and cord.x <= self.end.x 
        y_hit = cord.y == self.start.y
        return x_hit and y_hit


@dataclass
class SymbolCord:
    value: str
    start: Cord
    end: Cord

    def cord_hit(self, cord: Cord) -> bool:
        return cord == self.start


class EngineSchematic:
    schematic_str: str
    schematic: List[List[str]]
    number_cords: List[NumberCords]
    symbol_cords: List[SymbolCord]
    symbol_cords_map: Dict[Cord, SymbolCord]

    def __init__(self, schematic_str: str):
        number_pattern = re.compile(r'\d+')
        symbol_pattern = re.compile(r'[^0-9.]')

        schematic = []
        number_cords = []
        symbol_cords = []
        symbol_cords_map = {}
        for y, line in enumerate(schematic_str.split('\n')):
            schematic.append(list(line))

            for match in number_pattern.finditer(line):
                number_cords.append(NumberCords(
                    value=int(match.group()),
                    start=Cord(x=match.start(), y=y),
                    end=Cord(x=match.end() - 1, y=y)
                ))

            for match in symbol_pattern.finditer(line):
                sym_cord = SymbolCord(
                    value=match.group(),
                    start=Cord(x=match.start(), y=y),
                    end=Cord(x=match.end() - 1, y=y)
                )
                symbol_cords.append(sym_cord)
                symbol_cords_map[sym_cord.start] = sym_cord

        self.schematic_str = schematic_str
        self.schematic = schematic
        self.number_cords = number_cords
        self.symbol_cords = symbol_cords
        self.symbol_cords_map = symbol_cords_map

    def _cord_in_bounds(self, cord: Cord):
        x_len = len(self.schematic[0])
        y_len = len(self.schematic)
        if cord.x < 0 or (x_len - 1) < cord.x:
            return False

        if cord.y < 0 or (y_len - 1) < cord.y:
            return False

        return True

    def _get_adjacent_cords(self, num_cords: NumberCords) -> List[Cord]:
        y = num_cords.start.y
        adjecent_cords = []
        for y_delta in [-1, 0, 1]:
            for target_x in range(num_cords.start.x - 1, num_cords.end.x + 2):
                adj_cord = Cord(x=target_x, y=y + y_delta)
                if not self._cord_in_bounds(adj_cord):
                    continue
                elif num_cords.cord_hit(adj_cord):
                    continue
                else:
                    adjecent_cords.append(adj_cord)
        return adjecent_cords

    def get_part_numbers(self) -> List[int]:
        part_numbers = []
        for num_cords in self.number_cords:
            adjecent_cords = self._get_adjacent_cords(num_cords)
            for adj_cord in adjecent_cords:
                if adj_cord in self.symbol_cords_map:
                    part_numbers.append(num_cords.value)
                    break
        return part_numbers

    def get_gear_ratios(self) -> List[int]:

        # identify potential gears
        potential_gears_map: Dict[Cord, List[int]] = {}
        for cord, sym_cord in self.symbol_cords_map.items():
            if sym_cord.value == '*':
                potential_gears_map[cord] = []

        # map part numbers to potential gears
        for num_cords in self.number_cords:
            adjecent_cords = self._get_adjacent_cords(num_cords)
            for adj_cord in adjecent_cords:
                if adj_cord in potential_gears_map:
                    potential_gears_map[adj_cord].append(num_cords.value)

        # filter out non gears and get all gear ratios
        gear_ratios = []
        for cord, part_nums in potential_gears_map.items():
            if len(part_nums) != 2:
                continue

            gear_ratios.append(math.prod(part_nums))

        return gear_ratios


def answer(problem_input, level, test=None):
    engine_schematic = EngineSchematic(problem_input)

    if level == 1:
        return sum(engine_schematic.get_part_numbers())

    elif level == 2:
        return sum(engine_schematic.get_gear_ratios())


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
