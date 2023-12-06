import os
from aoc_utils import aoc_utils
from dataclasses import dataclass
from typing import List, Dict
import re
from queue import Queue
from collections import defaultdict


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11''', 'output': 13},
    {'level': 2, 'input': '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11''', 'output': 30},
]


@dataclass
class Card:
    id: int
    winning_numbers: List[int]
    card_numbers: List[int]

    @property
    def winning_number_matches(self) -> set:
        return set(self.winning_numbers).intersection(set(self.card_numbers))

    @property
    def num_matches(self) -> int:
        return len(self.winning_number_matches)

    @property
    def point_value(self) -> int:
        p = self.num_matches
        if p == 0:
            return 0
        return 2 ** (p - 1)


def answer(problem_input, level, test=None):
    card_pattern = re.compile(r'Card(\s+)(?P<card_id>\d+):(\s+)(?P<winning_numbers>[^\|]+)(\s+)\|(\s+)(?P<card_numbers>.+)')
    cards = []
    cards_map: Dict[int, Card] = {}
    for line in problem_input.split('\n'):
        line = line.strip()
        m = card_pattern.match(line)
        winning_numbers = list(map(int, re.split(r'\s+', m.group('winning_numbers').strip())))
        card_numbers = list(map(int, re.split(r'\s+', m.group('card_numbers').strip())))
        card = Card(
            id=int(m.group('card_id')),
            winning_numbers=winning_numbers,
            card_numbers=card_numbers
        )
        cards.append(card)
        cards_map[card.id] = card

    if level == 1:
        return sum([c.point_value for c in cards])

    elif level == 2:
        cards_count: Dict[int, int] = defaultdict(int)
        q = Queue()
        for c in cards:
            q.put(c)

        while not q.empty():
            card = q.get()
            cards_count[card.id] += 1

            card_copies = card.num_matches
            next_card_ids = list(range(card.id + 1, card.id + card_copies + 1))

            for next_card_id in next_card_ids:
                q.put(cards_map[next_card_id])

        return sum(cards_count.values())


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
