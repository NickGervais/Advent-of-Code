### Day 7: Handy Haversacks ###

class Bag():
    def __init__(self, color, sub_bags):
        self.color = color
        self.sub_bags = sub_bags


bags = {}

with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        line = line.rstrip()
        line = line.replace(' bags contain ', ',')
        line = line.replace(' bags', '')
        line = line.replace(' bag', '')
        line = line.replace(', ', ',')
        line = line.replace('.', '')
        bag_list = line.split(',')

        color = bag_list.pop(0)
        sub_bags = []
        for bag in bag_list:
            if bag == 'no other':
                break
            l = bag.split(' ')
            num = int(l[0])
            col = ' '.join(l[1:3])
            sub_bags.append([col, num])
        bags[color] = sub_bags


def part_1(bags):
    def has_color(target_color, cur_bag_color, bags):
        if cur_bag_color == target_color:
            return True
        else:
            return any([has_color(target_color, b[0], bags) for b in bags[cur_bag_color]])

    
    target = 'shiny gold'
    valid_bags = set()
    for color, sub_bags in bags.items():
        if color != target and has_color(target, color, bags):
            valid_bags.add(color)
    
    return len(valid_bags)

# print(part_1(bags))
# solution: 278

def part_2(bags):
    def count_nested_bags(cur_color, bags, memo = {}):
        if cur_color in memo:
            return memo[cur_color]
        
        cur_bag_has_count = 0
        for sub_bag in bags[cur_color]:
            num_sub_bag = sub_bag[1]
            cur_bag_has_count += num_sub_bag
            for _ in range(num_sub_bag):
                cur_bag_has_count += count_nested_bags(sub_bag[0], bags, memo)
        memo[cur_color] = cur_bag_has_count
        return cur_bag_has_count

    print(count_nested_bags('shiny gold', bags))

part_2(bags)
# solution: 45157