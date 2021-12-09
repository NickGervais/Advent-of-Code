import os
from aoc_utils import aoc_utils

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    l = []
    il = []
    lines = problem_input.split('\n')
    answers = lines.pop(0)
    # remove space
    lines.pop(0)

    lines = [line for line in lines if line]

    boards = []
    cur_board = {}
    for i in range(0, len(lines), 5):
        cur_board = {}
        ls = lines[i: i+5]
        for y, l in enumerate(ls):
            for x, c in enumerate(l.split()):
                cur_board[int(c)] = (x, y)
        boards.append(cur_board)
   
    
    print(len(boards))

    checked_boards = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]

    def is_board_valid(cb):
        has_solution = False
        for y in range(len(cb)):
            is_ones = True
            for x in range(len(cb[0])):
                if cb[y][x] != 1:
                    is_ones = False
                    continue
            if is_ones:
                has_solution = True
                break

        for x in range(len(cb[0])):
            is_ones = True
            for y in range(len(cb[0])):
                if cb[y][x] != 1:
                    is_ones = False
                    continue
            if is_ones:
                has_solution = True
                break

        return has_solution

    # print(is_board_valid([
    #     [1, 1, 1, 1, 0],
    #     [1, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0]
    # ]))
    
    # solved_board_i = None
    # last_answer = None
    # for c in answers.split(','):
    #     for i, board in enumerate(boards):
    #         if board.get(int(c)):
    #             x, y = board[int(c)]
    #             checked_boards[i][y][x] = 1

    #             if is_board_valid(checked_boards[i]):
    #                 solved_board_i = i
    #                 last_answer = int(c)
    #                 break
    #     if solved_board_i:
    #         break

    last_board_i = None
    last_answer = None
    valid_board_is = set()
    for c in answers.split(','):
        for i, board in enumerate(boards):
            if i not in valid_board_is and board.get(int(c)):
                x, y = board[int(c)]
                checked_boards[i][y][x] = 1

                if is_board_valid(checked_boards[i]):
                    if len(valid_board_is) == len(boards) - 1:
                        last_board_i = i
                        last_answer = int(c)
                        break
                    else:
                        valid_board_is.add(i)
        if last_board_i:
            break

    print(last_board_i)
    print(last_answer)

    unmarked_sum = 0
    for val, cords in boards[last_board_i].items():
        if checked_boards[last_board_i][cords[1]][cords[0]] == 0:
            unmarked_sum += int(val)
    
    sol = unmarked_sum * last_answer
    # print(sol)
    return (sol)



    # for line in problem_input.split('\n'):
    #     l.append(line.strip())
    #     il.append(int(line.strip()))

    # if level == 1:
    #     a = 0
    #     for i in il:
    #         a += i
    #     return

    # if level == 2:
    #     a = 0
    #     for i in il:
    #         a += i
    #     return

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
