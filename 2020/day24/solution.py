### Day 24: Lobby Layout ###

import re

directions = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        line = line.rstrip()
        directions.append(re.findall('(se|sw|e|w|ne|nw)', line))

print(directions)

