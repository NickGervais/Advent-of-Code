import os
from aoc_utils import aoc_utils

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(problem_input, level, test=None):
    l = []
    il = []
    for line in problem_input.split('\n'):
        l.append(line.strip())
        il.append(int(line.strip()))

    def get_common(j, l, which):
        bit = 0
        for i in l:
            if i[j] == '1':
                bit += 1
            else:
                bit -= 1
        
        if which == 'most_common':
            if bit > 0:
                return '1'
            elif bit < 0:
                return '0'
            else:
                return '1'
        else:
            if bit < 0:
                return '1'
            elif bit > 0:
                return '0'
            else:
                return '0'

    if level == 2:
        most_common = ''
        least_common = ''

        for j in range(len(l[0])):
            most_common += get_common(j, l, 'most_common')
            least_common += get_common(j, l, 'least_common')

        
        
        print(most_common, least_common)
        ox_set = set([i for i in l])
        co_set = set([i for i in l])

        # print(ox_set)

        for j in range(len(l[0])):
            j_most_common = get_common(j, list(ox_set), 'most_common')
            j_least_common = get_common(j, list(co_set), 'least_common')

            for i in l:
                if i in ox_set and i[j] != j_most_common and len(ox_set) > 1:
                    ox_set.remove(i)
                if i in co_set and i[j] != j_least_common and len(co_set) > 1:
                    co_set.remove(i)
        
        print(ox_set, co_set)
        return int(ox_set.pop(),2) * int(co_set.pop(), 2)

    if level == 2:
        a = 0
        for i in il:
            a += i
        return

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
