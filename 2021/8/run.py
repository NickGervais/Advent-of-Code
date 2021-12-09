import os
from aoc_utils import aoc_utils

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    l = []
    for line in problem_input.split('\n'):
        patterns, outputs = [i.strip() for i in line.split('|')]
        l.append((patterns.split(' '), outputs.split(' ')))
    
    if level == 1:
        total = 0
        for patterns, outputs in l:
            for o in outputs:
                if len(o) in (2, 3, 4, 7):
                    total += 1
        return total
    if level == 2:
        SEGMENTS_TO_DIGITS = {
            '0,1,2,4,5,6': 0,
            '2,5': 1,
            '0,2,3,4,6': 2,
            '0,2,3,5,6': 3,
            '1,2,3,5': 4,
            '0,1,3,5,6': 5,
            '0,1,3,4,5,6': 6,
            '0,2,5': 7,
            '0,1,2,3,4,5,6': 8,
            '0,1,2,3,5,6': 9
        }

        def char_in_count(n, char, ps, count):
            if n == 'not':
                for p in ps:
                    if len(p) == count and char in p:
                        return False
                return True
            else:
                # needs to be in all
                for p in ps:
                    if len(p) == count and char not in p:
                        return False
                return True

        def is_safe(char, seg_i, ps):
            if seg_i == 0:
                return (char_in_count('not', char, ps, 2)) and (char_in_count('in', char, ps, 3)) and (char_in_count('not', char, ps, 4)) and (char_in_count('in', char, ps, 5)) and (char_in_count('in', char, ps, 6))
            elif seg_i == 1:
                return (char_in_count('not', char, ps, 2)) and (char_in_count('not', char, ps, 3)) and (char_in_count('in', char, ps, 4)) and (char_in_count('in', char, ps, 6))
            elif seg_i == 2:
                return (char_in_count('in', char, ps, 2)) and (char_in_count('in', char, ps, 3)) and (char_in_count('in', char, ps, 4))
            elif seg_i == 3:
                return (char_in_count('not', char, ps, 2)) and (char_in_count('not', char, ps, 3)) and (char_in_count('in', char, ps, 4)) and (char_in_count('in', char, ps, 5))
            elif seg_i == 4:
                return (char_in_count('not', char, ps, 2)) and (char_in_count('not', char, ps, 3)) and (char_in_count('not', char, ps, 4))
            elif seg_i == 5:
                return (char_in_count('in', char, ps, 2)) and (char_in_count('in', char, ps, 3)) and (char_in_count('in', char, ps, 4)) and (char_in_count('in', char, ps, 6))
            elif seg_i == 6:
                return (char_in_count('not', char, ps, 2)) and (char_in_count('not', char, ps, 3)) and (char_in_count('not', char, ps, 4)) and (char_in_count('in', char, ps, 5)) and (char_in_count('in', char, ps, 6))


        def extend_solution(seg_chars, rem_chars, seg_i, ps):
            if seg_i >= len(seg_chars):
                return True

            for c in rem_chars:
                if is_safe(c, seg_i, ps):
                    new_rem_chars = [i for i in rem_chars if i != c]
                    seg_chars[seg_i] = c

                    if extend_solution(seg_chars, new_rem_chars, seg_i + 1, ps):
                        return True

                    seg_chars[seg_i] = None
            return False

        total = 0
        for patterns, outputs in l:
            seg_keys = [None for _ in range(7)]
            found_solution = extend_solution(seg_keys, ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 0, patterns)
            assert found_solution
            num = ''
            for o in outputs:
                segs = [seg_keys.index(c) for c in o]
                num += str(SEGMENTS_TO_DIGITS[','.join([str(i) for i in sorted(segs)])])
            total += int(num)
            
        return total

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
