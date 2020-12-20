### Day 13:  ###

rules = {}
with open('rules.txt', 'r') as input:
    for i, line in enumerate(input):
        line = line.rstrip()
        rule_i, rule = line.split(': ')
        rule_ors = rule.split(' | ')
        final_rules = []
        for r in rule_ors:
            final_rules.append([j.replace('"', '') for j in r.split(' ')])
        rules[rule_i] = final_rules

inputs = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        inputs.append(line.rstrip())

import re

def build_pattern(rules, rule_i):
    full_pattern = []
    for rule_ors in rules[rule_i]:
        cur_pattern = []
        for rule_i2 in rule_ors:
            if not rule_i2.isdigit():
                return rule_i2
            else:
                cur_pattern.append(build_pattern(rules, rule_i2))
        full_pattern.append(''.join(cur_pattern))
    return f"({'|'.join(full_pattern)})"


def part_1(rules, inputs):
    pattern = build_pattern(rules, '0')

    total_valid = 0
    for i in inputs:
        if re.match(f'^{pattern}$', i):
            total_valid += 1

    print(total_valid)

part_1(rules, inputs)







# def is_match(rules, rule, val):
    
#     pattern = f'^{}$'
#     result = re.match(r'^$')

# def part_1(rules, inputs):

