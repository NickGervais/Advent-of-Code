### Day 8: Handheld Halting ###

instructions = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        instructions.append(line.rstrip())

def part_1(instructions):
    acc = 0

    seen = set()
    i = 0
    while not i in seen:
        seen.add(i)
        operation, argument = instructions[i].split(' ')
        if operation == 'acc':
            acc = eval(f'{acc}{argument}')
            i += 1
        elif operation == 'jmp':
            i = eval(f'{i}{argument}')
        elif operation == 'nop':
            i += 1
    
    return acc

# print(part_1(instructions))
# solution: 1749


class Node():
    def __init__(self, index, operation, argument, children):
        self.index = index
        self.operation = operation
        self.argument = argument
        self.children = children

    def to_dict(self):
        return {
            'index': self.index,
            'operation': self.operation,
            'argument': self.argument,
            'children': self.children
        }

def find_path(nodes, cur_index, goal_index, seen_set, on_alt_path):
    if cur_index is None or cur_index in seen_set:
        return False, 0
    elif cur_index == goal_index: 
        return True, 0        
    seen_set.add(cur_index)

    cur_node = nodes[cur_index]
    acc_value_arg = cur_node.argument if cur_node.operation == 'acc' else '+0'

    if on_alt_path:
        found, val = find_path(nodes, cur_node.children[0], goal_index, seen_set.copy(), on_alt_path)
        if found:
            return True, eval(f'{val}{acc_value_arg}')
    else:
        found, val = find_path(nodes, cur_node.children[0], goal_index, seen_set.copy(), False)
        if found:
            return True, eval(f'{val}{acc_value_arg}')
        found, val = find_path(nodes, cur_node.children[1], goal_index, seen_set.copy(), True)
        if found:
            return True, eval(f'{val}{acc_value_arg}')
    return False, 0


def part_2(instructions):
    # create map
    nodes = {}
    for i, instruction in enumerate(instructions):
        operation, argument = instruction.split(' ')
        children = [None, None]
        if operation in ['nop', 'jmp']:
            children[0] = i + 1 if operation == 'nop' else eval(f'{i}{argument}')
            children[1] = i + 1 if operation == 'jmp' else eval(f'{i}{argument}')
        elif operation == 'acc':
            children[0] = i + 1
        nodes[i] = Node(i, operation, argument, children)

    # depth first search on map
    found, acc_val = find_path(nodes, 0, len(instructions), set(), False)
    print(found, acc_val)

part_2(instructions)
# solution: 515