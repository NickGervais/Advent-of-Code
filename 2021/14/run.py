import os
from aoc_utils import aoc_utils
from collections import defaultdict, Counter

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def calc_count_map(count_map, template):
    # turn pairs into count per each character.
    # ex: {'NC': 2, 'CB': 1} -> {'N': 2, 'C': 3, 'B' 1}
    char_count_map = defaultdict(int)
    for pair, count in count_map.items():
        char_count_map[pair[0]] += count
        char_count_map[pair[1]] += count

    # in the previous step we counted each character twice.
    # except for the last and first character in the string.
    # So if the character is either the first or last string, add 1 to the total
    # then divide each value by 2. This accounts for our over counting.

    new_char_count_map = defaultdict(int)
    for char, count in char_count_map.items():
        if char in [template[0], template[-1]]:
            count += 1
        new_char_count_map[char] = count / 2
    print(new_char_count_map)
    
    # lastly find the smallest and largest counts.
    max_val = -1
    min_val = float('inf')
    for char, count in new_char_count_map.items():
        if count > max_val:
            max_val = count
        elif count < min_val:
            min_val = count

    result = int(max_val) - int(min_val)
    # print(f'{int(max_val)} - {min_val} = {result}')
    return result

def answer(problem_input, level, test=None):
    lines = problem_input.split('\n')
    template = [i for i in lines[0]]
    pairs_map = defaultdict(list)
    pair_map = {}
    for l in lines[2:]:
        pair, middle = l.split(' -> ')
        pair_map[pair] = middle
        pairs_map[pair].extend([f'{pair[0]}{middle}', f'{middle}{pair[1]}'])

    count_map = defaultdict(int)
    for i in range(len(template) -1):
        pair = ''.join(template[i:i+2])
        count_map[pair] += 1

    if level == 1 or level == 2:
        for epoch in range(40):
            if epoch == 10 and level == 1:
                break
            new_count_map = defaultdict(int)
            for pair, count in count_map.items():
                next_pairs = pairs_map[pair]
                for next_pair in next_pairs:
                    new_count_map[next_pair] += count
            count_map = new_count_map
            # print(count_map)
        return calc_count_map(count_map, template)

        # print("\n\n")
        # for _ in range(5):
        #     new_template = []
        #     for i in range(len(template) - 1):
        #         pair = template[i:i+2]
        #         insert_char = pair_map[''.join(pair)]
        #         new_template.extend([pair[0], insert_char])
        #     new_template.append(template[-1])
        #     template = new_template
        #     print(''.join(template))
        
        #     res = Counter(template)
        #     max_val = template.count(max(res, key = res.get))
        #     min_val = template.count(min(res, key = res.get))
        #     result = max_val - min_val
        #     print(f'{max_val} - {min_val} = {result}')
        # return result

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
