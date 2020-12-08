### Day 9: Sensor Boost ###
from intcode_computer import IntcodeComputer

og_intcode = []
with open('input.txt', 'r') as problem_input:
    for i, line in enumerate(problem_input):
        og_intcode = [int(val) for val in line.split(",")]

## Part One ##
comp1 = IntcodeComputer(list(og_intcode), 1)
result1 = comp1.run_intcode(1)
print(f"Part 1: {result1}")

## Part Two ##
comp2 = IntcodeComputer(list(og_intcode), 2)
result2 = comp2.run_intcode(2)
print(f"Part 2: {result2}")