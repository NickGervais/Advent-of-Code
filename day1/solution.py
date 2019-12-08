### Day 1: The Tyranny of the Rocket Equation ####

## PART 1 ##
# import math

# result_1 = 0

# with open('input.txt', 'r') as input:
#     for i, line in enumerate(input):
#         mass = int(line)
#         fuel_required = math.floor(mass / 3) - 2
#         result_1 += fuel_required

# print(f"Part 1: {result_1}")

## PART 2 ##

import math

def calculate_fuel_for_mass(mass: int) -> int:
    fuel_mass = math.floor(mass / 3) - 2
    if fuel_mass <= 0:
        return 0
    else:
        return fuel_mass + calculate_fuel_for_mass(fuel_mass)

result_2 = 0

with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        mass = int(line)
        result_2 += calculate_fuel_for_mass(mass)

print(f"Part 2: {result_2}")
