import os
from aoc_utils import aoc_utils
import math
from pydantic import BaseModel
from typing import List
import re


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
    {
        'level': 1,
        'input': """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""",
        "output": 8
    },
    {
        'level': 2,
        'input': """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""",
        "output": 2286
    },
]


class Handfull(BaseModel):
    red: int = 0
    blue: int = 0
    green: int = 0

    def meets_criteria(self, criteria: "Handfull") -> bool:
        return self.red <= criteria.red and self.blue <= criteria.blue and self.green <= criteria.green

    @property
    def power(self) -> int:
        non_zero_fields = [num for num in self.model_dump().values() if num != 0]
        return math.prod(non_zero_fields)


class Game(BaseModel):
    id: int
    grabs: List[Handfull]


def answer(problem_input, level, test=None):
    games = []
    lines = []
    for line in problem_input.split('\n'):
        line = line.strip()
        lines.append(line)

        game_id_raw, grabs_str = line.split(':')
        game_id = re.findall(r"Game (\d+)", game_id_raw)[0]
        grabs_str = [s.strip() for s in grabs_str.split(';')]

        grabs = []
        for grab_str in grabs_str:
            handfull_tuples = re.findall(r"(?P<count>\d+) (?P<color>\w+)", grab_str)

            handfull_dict = {}
            for count, color in handfull_tuples:
                handfull_dict[color] = count

            grabs.append(Handfull.model_validate(handfull_dict))

        games.append(Game(id=game_id, grabs=grabs))

    # 12 red cubes, 13 green cubes, and 14 blue cubes
    criteria = Handfull(red=12, green=13, blue=14)
    if level == 1:
        possible_game_ids = []
        for game in games:

            possible_game = True
            for handfull in game.grabs:
                if not handfull.meets_criteria(criteria):
                    possible_game = False

            if possible_game:
                possible_game_ids.append(game.id)

        return sum(possible_game_ids)

    elif level == 2:
        criteria = Handfull(red=12, green=13, blue=14)
        powers = []

        for game in games:
            min_set = Handfull(red=-1, green=-1, blue=-1)

            for handfull in game.grabs:
                min_set = Handfull(
                    red=max(min_set.red, handfull.red),
                    green=max(min_set.green, handfull.green),
                    blue=max(min_set.blue, handfull.blue)
                )

            powers.append(min_set.power)

        return sum(powers)


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
