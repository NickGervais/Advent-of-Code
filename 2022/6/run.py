import os

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def answer(level):
    lines = []
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            lines.append(line.strip())

    sequence = lines[0]

    if level == 1:
        unique_char_len = 4

    elif level == 2:
        unique_char_len = 14

    i = unique_char_len
    while i < len(sequence):
        if len(set(sequence[i-unique_char_len:i])) == unique_char_len:
            return i
        i += 1
    return None

print(answer(1))
