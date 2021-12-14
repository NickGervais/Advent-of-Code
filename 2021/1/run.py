from aoc_utils import aoc_utils

year = 2021
day = 1

problem_input = aoc_utils.fetch_and_save(year, day)

test_cases = [
#     {'level': 1, 'input': [199,
# 200,
# 208,
# 210,
# 200,
# 207,
# 240,
# 269,
# 260,
# 263], 'output': 7},
# {'level': 2, 'input': [199,
# 200,
# 208,
# 210,
# 200,
# 207,
# 240,
# 269,
# 260,
# 263], 'output': 7}
]

def answer(input, level, test=None):
    if not isinstance(input, list):
        input = [int(i) for i in input.split('\n')]
    
    if level == 1:
        total_larger = 0
        for i in range(1, len(input)):
            if input[i] > input[i-1]:
                total_larger += 1

        return total_larger
    if level == 2:
        total_larger = 0
        for i in range(1, len(input)):
            if sum(input[i:i+3]) > sum(input[i-1:i+2]):
                total_larger += 1

        return total_larger

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
