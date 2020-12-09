### Day 6: Custom Customs ###

def part_1():
    group_sets = []
    cur_group = set()
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            line = line.rstrip()
            if not line or line.isspace():
                group_sets.append(cur_group)
                cur_group = set()
            else:
                for char in line:
                    cur_group.add(char)
        group_sets.append(cur_group)

    total = 0
    for group in group_sets:
        total += len(group)
    
    return total

print(part_1())
# solution: 6763


def part_2():
    group_dicts = []
    cur_group = {
        'total_people': 0
    }
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            line = line.rstrip()
            if not line or line.isspace():
                group_dicts.append(cur_group)
                cur_group = {
                    'total_people': 0
                }
            else:
                cur_group['total_people'] += 1
                for char in line:
                    if char in cur_group:
                        cur_group[char] += 1
                    else:
                        cur_group[char] = 1
        group_dicts.append(cur_group)

    total = 0
    for group in group_dicts:
        num_yes = 0
        total_people = group.pop('total_people')
        for key, val in group.items():
            if val == total_people:
                num_yes += 1
        total += num_yes
    
    return total

print(part_2())
# solution: 3512
            