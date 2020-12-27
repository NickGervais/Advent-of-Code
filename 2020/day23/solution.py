### Day 23: Crab Cups ###

class Cups():
    from itertools import cycle

    def __init__(self, cups):
        self.cups_list = cups
        self.cups = {val: i for i, val in enumerate(cups)}
        self.current_cup = cups[0]
        self.picked_cups = []
        self.destination_cup = None
    
    def set_picked_cups(self):
        current_cup_i = self.cups[self.current_cup]

        picked_indexes = [self.calc_index(current_cup_i + i) for i in range(1, 4)]
        
        new_cups = {}
        picked = []
        cur_i = 0
        for val, i in self.cups.items():
            if i not in picked_indexes:
                new_cups[val] = cur_i
                cur_i += 1
            else:
                picked.append(val)

        self.cups = new_cups
        self.picked_cups = picked
        return self.picked_cups

    def calc_index(self, index):
        return index % len(self.cups)

    def set_destination_cup(self):
        destination_cup = None

        min_cup = min(self.cups.keys())
        max_cup = max(self.cups.keys())

        cup_i = self.current_cup - 1

        while destination_cup is None:
            if cup_i < min_cup: 
                cup_i = max_cup
            if cup_i in self.cups:
                destination_cup = cup_i
            else:
                cup_i -= 1

        self.destination_cup = destination_cup
        # print(f'destination: {self.destination_cup}')
        return self.destination_cup

    def place_picked_cups(self):
        destination_cup = self.set_destination_cup()
        split_i = self.cups[destination_cup] + 1 
        new_cups = {val: split_i + i for i, val in enumerate(self.picked_cups)}
        for val, i in self.cups.items():
            if i <= split_i:
                new_cups[val] = i
            else:
                new_cups[val] = i + 3

        self.cups = new_cups
    
    def run_move(self):
        # print(f"cups: {', '.join([f'({j})' if j == self.current_cup else str(j) for j in self.cups])}")
        self.set_picked_cups()
        # print(f'pick up: {self.picked_cups}')
        self.place_picked_cups()

        cur_cup_i = self.cups[self.current_cup]
        next_cur_cup_i = self.calc_index(cur_cup_i + 1)

        key_list = list(self.cups.keys())
        val_list = list(self.cups.values())

        self.current_cup = key_list[val_list.index(next_cur_cup_i)]


def part_1(cups):
    circle = Cups([int(i) for i in cups])

    for i in range(100):
        # print(f'-- move {i} --')
        circle.run_move()
        # print('')
    
    # print('-- final --')
    # print(f"cups: {', '.join([f'({j})' if j == circle.current_cup else str(j) for j in circle.cups])}")

    result = ''
    key_list = list(circle.cups.keys())
    val_list = list(circle.cups.values())
    start_index = circle.cups[1]
    for i in range(start_index+1, len(circle.cups)+start_index):
        result += str(key_list[val_list.index(i)])
    print(result)



part_1('496138527')
# solution: 69425837

def part_2(cups):
    cups = [int(i) for i in cups]
    max_cup = max(cups)
    for i in range(max_cup+1, 1000001):
        cups.append(i)
    circle = Cups(cups)
    print('start moves')

    for _ in range(10000000):
        circle.run_move()
    
    start_index = circle.cups.index(1)
    target_cups = [
        circle.cups[circle.calc_index(start_index+1)],
        circle.cups[circle.calc_index(start_index+2)]
    ]
    print(target_cups[0] * target_cups[1])

# part_2('389125467')