import os
from aoc_utils import aoc_utils
from dataclasses import dataclass
import re
import math


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)''', 'output': 2},
    {'level': 2, 'input': '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)''', 'output': 6},
]


@dataclass
class Node:
    value: str
    left: str
    right: str


def answer(problem_input, level, test=None):
    instructions, network_lines = problem_input.split('\n\n')
    instruct_len = len(instructions)

    network = {}
    for line in network_lines.split('\n'):
        line = line.strip()
        m = re.match(r'(?P<value>\w+) \= \((?P<left>\w+), (?P<right>\w+)\)', line)
        node = Node(value=m.group('value'), left=m.group('left'), right=m.group('right'))
        network[node.value] = node

    if level == 1:

        target_value = 'ZZZ'
        current = network['AAA']
        steps = 0
        instruction_index = 0

        while current.value != target_value:
            instruction = instructions[instruction_index % instruct_len]
            if instruction == 'L':
                current = network[current.left]
            else:
                current = network[current.right]
            steps += 1
            instruction_index += 1

        return steps

    elif level == 2:

        # Brute Force Solution:
        # current_nodes = [node for value, node in network.items() if value[-1] == 'A']
        # steps = 0
        # instruction_index = 0
        # while not all([node.value[-1] == 'Z' for node in current_nodes]):
        #     instruction = instructions[instruction_index % instruct_len]
        #     for ni, current_node in enumerate(current_nodes):
        #         if instruction == 'L':
        #             current_nodes[ni] = network[current_node.left]
        #         else:
        #             current_nodes[ni] = network[current_node.right]
        #     steps += 1
        #     instruction_index += 1
        # return steps

        # Optimized Solution:
        # find each starting node to first end node step length, this is the cycle length for this node
        # once you have the cycle length for each starting node, the answer will be the least common multiple of each of these cycle lengths.
        starting_nodes = [node for value, node in network.items() if value[-1] == 'A']
        node_steps = [0 for _ in starting_nodes]

        for i, node in enumerate(starting_nodes):
            current_node = node
            steps = 0
            instruction_index = 0

            while current_node.value[-1] != 'Z':
                instruction = instructions[instruction_index % instruct_len]
                if instruction == 'L':
                    current_node = network[current_node.left]
                else:
                    current_node = network[current_node.right]
                steps += 1
                instruction_index += 1

            node_steps[i] = steps

        return math.lcm(*node_steps)


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
