import os
from aoc_utils import aoc_utils
import time

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    l = []
    for line in problem_input.split('\n'):
        l.append(line.strip())

    closing_to_opening = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    opening_to_closing = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    completion_score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    if level == 1 or level == 2:
        incomplete_lines = []
        score = 0
        for i in l:
            q = []
            corrupted = False
            for c in i:
                if c in closing_to_opening:
                    if len(q) > 0 and q[-1] != closing_to_opening[c]:
                        score += score_map[c]
                        corrupted = True
                        break
                    else:
                        q.pop(-1)
                else:
                    q.append(c)
            if not corrupted:
                incomplete_lines.append(i)
        print(score)

        score2s = []
        for line in incomplete_lines:
            q = []
            for c in line:
                if c in closing_to_opening:
                    q.pop(-1)
                else:
                    q.append(c)
            score2 = 0
            for opening_c in reversed(q):
                score2 = (score2*5) + completion_score_map[opening_to_closing[opening_c]]
            score2s.append(score2)
        
        score2s.sort()
        print(score2s[len(score2s)//2])

        return score2s[len(score2s)//2]

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
