import os
from aoc_utils import aoc_utils
from collections import defaultdict
from itertools import cycle

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def play_turn(start_i, die):
    spaces_moved = 0
    for _ in range(3):
        roll = next(die)
        spaces_moved += roll
    

    new_i = start_i + spaces_moved
    return new_i
    


def answer(problem_input, level, test=None):
    problem_input = problem_input.split('\n')
    p1 = int(problem_input[0].replace('Player 1 starting position: ', ''))
    p2 = int(problem_input[1].replace('Player 2 starting position: ', ''))

    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    scores = {
        'p1': 0,
        'p2': 0
    }

    pos_index = {
        'p1': p1 - 1, # 3
        'p2': p2 - 1, # 7
    }

    whos_turn = 'p1'

    if level == 1:
        die = cycle(range(1, 101))
        die_rolls = 0

        winner = None
        loser = None

        while True:
            new_pos_index = play_turn(pos_index[whos_turn], die)
            die_rolls += 3

            scores[whos_turn] += board[new_pos_index % len(board)]
            
            # print(whos_turn, ':', scores[whos_turn], pos_index[whos_turn], new_pos_index)
            
            pos_index[whos_turn] = new_pos_index
            next_whos_turn = 'p2' if whos_turn == 'p1' else 'p1'
            
            if scores[whos_turn] >= 1000:
                winner = whos_turn
                loser = next_whos_turn
                break

            whos_turn = next_whos_turn

        return scores[loser] * (die_rolls)
    
    if level == 2:
        die_sides = 3
        pass


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
