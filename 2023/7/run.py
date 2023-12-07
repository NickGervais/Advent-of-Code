import os
from aoc_utils import aoc_utils
from dataclasses import dataclass
from typing import List, Dict
from collections import defaultdict


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483''', 'output': 6440},
    {'level': 2, 'input': '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483''', 'output': 5905},
]

CARD_STRENGTHS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_STRENGTHS_2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


@dataclass
class Hand:
    cards: List[str]
    bid: int

    wildcard: str = 'J'

    @property
    def strength(self):
        card_groupings: Dict[str, int] = defaultdict(int)
        for card in self.cards:
            card_groupings[card] += 1

        # Five of a kind
        if 5 in card_groupings.values():
            return 7
        # Four of a kind
        if 4 in card_groupings.values():
            return 6
        # Full house
        if 3 in card_groupings.values() and 2 in card_groupings.values():
            return 5
        # Three of a kind
        if 3 in card_groupings.values():
            return 4
        # Two pair
        if list(card_groupings.values()).count(2) == 2:
            return 3
        # One pair
        if 2 in card_groupings.values():
            return 2
        # High card, where all cards' labels are distinct: 23456
        if len(card_groupings.values()) == 5:
            return 1

    @property
    def strength_2(self):
        card_groupings: Dict[str, int] = defaultdict(int)
        for card in self.cards:
            card_groupings[card] += 1

        num_wilds = 0
        if self.wildcard in card_groupings:
            num_wilds = card_groupings.pop(self.wildcard)

        sorted_group_counts = sorted(list(card_groupings.values()), reverse=True)
        if len(sorted_group_counts) == 0:
            sorted_group_counts.append(num_wilds)
        else:
            sorted_group_counts[0] += num_wilds  # is this always the best?

        # Five of a kind
        if 5 == sorted_group_counts[0]:
            return 7
        # Four of a kind
        if 4 == sorted_group_counts[0]:
            return 6
        # Full house
        if 3 == sorted_group_counts[0] and 2 == sorted_group_counts[1]:
            return 5
        # Three of a kind
        if 3 == sorted_group_counts[0]:
            return 4
        # Two pair
        if 2 == sorted_group_counts[0] and 2 == sorted_group_counts[1]:
            return 3
        # One pair
        if 2 == sorted_group_counts[0]:
            return 2
        # High card, where all cards' labels are distinct: 23456
        if len(sorted_group_counts) == 5:
            return 1


class CamelCards:

    def __init__(self, text_input: str):
        hands: List[Hand] = []

        for line in text_input.split('\n'):
            raw_hand, raw_bid = line.strip().split(' ')
            hands.append(Hand(
                cards=list(raw_hand),
                bid=int(raw_bid)
            ))
        self.hands = hands

    @property
    def ranked_cards(self):
        return sorted(self.hands, key=lambda hand: (hand.strength, CARD_STRENGTHS.index(hand.cards[0]), CARD_STRENGTHS.index(hand.cards[1]), CARD_STRENGTHS.index(hand.cards[2]), CARD_STRENGTHS.index(hand.cards[3]), CARD_STRENGTHS.index(hand.cards[4])))

    @property
    def ranked_cards_2(self):
        return sorted(self.hands, key=lambda hand: (hand.strength_2, CARD_STRENGTHS_2.index(hand.cards[0]), CARD_STRENGTHS_2.index(hand.cards[1]), CARD_STRENGTHS_2.index(hand.cards[2]), CARD_STRENGTHS_2.index(hand.cards[3]), CARD_STRENGTHS_2.index(hand.cards[4])))


def answer(problem_input, level, test=None):
    camelCards = CamelCards(problem_input)

    if level == 1:
        return sum([card.bid * (i + 1) for i, card in enumerate(camelCards.ranked_cards)])

    elif level == 2:
        return sum([card.bid * (i + 1) for i, card in enumerate(camelCards.ranked_cards_2)])


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
